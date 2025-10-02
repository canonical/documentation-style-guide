# This is a simple test suite for our Vale rules

import pytest
import subprocess
import os
import json
import yaml

vale_configuration = os.path.abspath(os.path.join(os.path.realpath(__file__), "../../vale.ini"))
test_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), "../"))
test_data = yaml.safe_load(open(os.path.join(test_dir + "/expected_output.yml"), 'r'))

class ValeTestConfig:
    def __init__(self, target, config=vale_configuration, filter="", output="JSON"):
        self.target = target
        self.config = config
        self.filter = filter
        self.output = output

    def run(self):
        print(vars(self))
        out, err = subprocess.Popen(
            ["vale", "--config", self.config, "--filter", self.filter, "--output", self.output, self.target],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            text = True,
        ).communicate()

        return json.loads(out)
    

@pytest.mark.parametrize("test_file, test_data", [
    ("test000.rst", test_data["test000.rst"])
])
def test_vale_rule(test_file, test_data):
    print(test_file)
    print(test_data)
    target = os.path.join(test_dir + "/" + test_file)
    filter = f'.Name=="Canonical.{test_data["rule"]}"'
    case = ValeTestConfig(target, filter=filter).run()[target]
    print(case)

    assert len(case) == len(test_data["matches"])
    for match in case:
        assert match["Match"] in test_data["matches"]
