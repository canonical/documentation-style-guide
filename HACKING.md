In this guide:

- [Guidance for maintainers of the rules](#guidance-for-maintainers-of-the-rules)
    - [Add test cases for a rule](#add-test-cases-for-a-rule)
    - [Run all test cases](#run-the-test-cases)
    - [Run selected test cases](#run-selected-test-cases)
- [Guidance for maintainers of the testing code](#guidance-for-maintainers-of-the-testing-code)

# Guidance for maintainers of the rules

See first: [Introduction to Vale rule development](getting-started.md)

## Add test cases for a rule

Make sure that the rule has suitable test cases in [tests/data/manifest.yml](tests/data/manifest.yml).

## Run all test cases

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

## Run selected test cases

Behind the scenes, we're using [pytest](https://docs.pytest.org/en/stable/) to run each test case.

To run the test cases for a particular rule, such as `003-Ubuntu-names-versions`:

- **If uv is installed**

    ```text
    uv run --directory tests pytest -vv -k 003
    ```

- **If uv is not installed**

    ```text
    # (Provided the working dir is 'tests' and the virtual environment is active)
    pytest -vv -k 003
    ```

# Guidance for maintainers of the testing code

The code in the `tests` directory uses Python with [pytest](https://docs.pytest.org/en/stable/). We require the code to be well-formatted and pass static checks.

Our tools of choice are:

- [ruff](https://docs.astral.sh/ruff/) for formatting and checking code conventions
- [pyright](https://microsoft.github.io/pyright/) for checking types

If you've already installed ruff, you should be able to use it in the `tests` directory with no trouble. pyright is less straightforward, as it needs to be run in a virtual environment that contains the testing code's dependencies.

Instead of manually running these tools, we strongly recommend that you install [uv](https://docs.astral.sh/uv/) and use `make` in the `tests` directory.

| Command       | Purpose                                                       |
|---------------|---------------------------------------------------------------|
| `make format` | Use ruff to format the testing code                           |
| `make lint`   | Use ruff to check code conventions and pyright to check types |
| `make run`    | Use pytest to run the test cases for every rule               |
