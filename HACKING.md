# Guidance for maintainers of the rules

See first: [Introduction to Vale rule development](getting-started.md) (TODO: needs reviewing)

## Add test cases for a rule

Make sure that the rule has suitable test cases in [tests/data/manifest.yml](tests/data/manifest.yml).

## Run the test cases

We recommend that you first install [uv](https://docs.astral.sh/uv/). To install uv on Ubuntu:

```
sudo snap install astral-uv --classic
```

To run the test cases for every rule:

- **If uv is installed**

    ```text
    make -C tests run
    ```

- **If uv is not installed**

    ```text
    cd tests
    python3 -m venv .venv
    . .venv/bin/activate
    pip install -e .
    make run
    ```

Behind the scenes, we're using [pytest](https://docs.pytest.org/en/stable/) to run each test case.

To run the test cases for a particular rule, such as `003-Ubuntu-names-versions`:

- **If uv is installed**

    ```text
    uv run --directory tests pytest -vv -k 003
    ```

- **If uv is not installed**

    ```text
    # (provided the working dir is 'tests' and the virtual environment is active)
    pytest -vv -k 003
    ```

# Guidance for maintainers of the testing code

TODO
