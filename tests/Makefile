# If we can, use uv (https://docs.astral.sh/uv/) to manage a virtual environment and run commands.
# Otherwise, require an active virtual environment and directly run commands.
uv := $(shell which uv)
ifdef uv
runner = uv run
else ifndef VIRTUAL_ENV
prerun = $(error You have not activated a virtual environment)
endif

.PHONY: help run format lint clean

# Put the help target first, so that 'make' shows it by default.
help:
	@echo "Test the Vale rules                    make run"
	@echo "Format the testing code                make format"
	@echo "Check for errors in the testing code   make lint"

run:
	$(prerun)
	$(runner) pytest -vv

format:
	$(prerun)
	$(runner) ruff format

lint:
	$(prerun)
	$(runner) ruff check
	$(runner) ruff format --diff
	$(runner) pyright
