# This is a simple test suite for our Vale rules

import pytest
import subprocess
import os
import json
import yaml

file = os.path.realpath(__file__)
test_dir = os.path.dirname(file)
vale_configuration = os.path.join(test_dir, "../vale.ini")


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
    
def pytest_generate_tests(metafunc):
    test_file = yaml.safe_load(open(os.path.join(test_dir + "/expected_output.yml"), 'r'))
    parsed = [(key, value) for key, value in test_file.items()]
    if "generated_test_data" in metafunc.fixturenames:
        metafunc.parametrize('generated_test_data', parsed)

def test_vale_rule(generated_test_data):
    print(generated_test_data[0])
    print(generated_test_data[1])
    target = os.path.join(test_dir + "/" + generated_test_data[0])
    filter = f'.Name=="Canonical.{generated_test_data[1]["rule"]}"'
    case = ValeTestConfig(target, filter=filter).run()[target]
    print(case)

    assert len(case) == len(generated_test_data[1]["matches"])
    for match in case:
        assert match["Match"] in generated_test_data[1]["matches"]


# if __name__ == "__main__":
