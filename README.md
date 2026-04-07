# Canonical documentation style guide

This repository contains the documentation and the Vale rules for the documentation style guide.

The style guide itself is written in Markdown and contained in the `en` directory.

It is published online at: [docs.ubuntu.com/styleguide/en](https://docs.ubuntu.com/styleguide/en)

## The Vale rules

The Vale linter operates from a series of rules. These are defined in individual YAML files, grouped into 'Styles'.

### Manual check

To manually check your documentation with Vale rules use the following steps:

1. Install Vale
    ```shell
    sudo snap install vale
    ```
2. Clone this repository.
3. Run Vale with the configuration file `vale.ini` from this repository for testing your documentation source files: 
  
    ```shell
    vale --config ~/documentation-style-guide/vale.ini ~/product/docs/
    ```

For automation, see the [Canonical Style GitHub action](#the-canonical-style-github-action).

### Adding to the rules

Anyone is welcome to submit a PR to add additional rules. However, no additions will be considered unless they are part of the Canonical Style Guide as found at the website above.

For a reference on rule syntax, see the Vale [documentation on Styles][Vale styles].

If you are completely new to developing Vale rules, see this [introductory guide](getting-started.md). 

### Testing the rules

This repo includes automated tests of the rules, which you can run locally, and which run in CI. See [Guidance for maintainers of the rules](HACKING.md).

### Using the rules

The Vale rules are published here so that they can be used in any workflow anywhere. You can run Vale locally, as part of CI or in a GitHub workflow - all you need is Vale, a configuration file (which you can also copy from this repository) and the Canonical Styles. Two common scenarios are also catered for more directly here, as detailed below.

## The Canonical Style GitHub action

This repository also includes a file, `action.yml`, which is the basis of a GitHub action to automatically run Vale checks on incoming pull requests. 

### Using the GitHub action in a workflow

Your repository can make use of the action in a workflow. An example workflow is included in this repository and is demonstrated here. Note that the style guide action is merely part of a functioning workflow.

```yaml
on: [pull_request]

jobs:
  vale:
    name: Style checker
    runs-on: ubuntu-22.04
    defaults:
        run:
            shell: bash
            working-directory: .
    steps:
        - name: Checkout repo to runner
          uses: actions/checkout@v3
        - name: Install styles
          uses: canonical/documentation-style-guide@main
        - name: Run Vale tests
          uses: errata-ai/vale-action@reviewdog
          with:
            files: ./docs
            fail_on_error: true
```

In the example above, the workflow is organised as a single job. This is important as the actions rely on persistence through the run.
There are three job steps:
 - The github/checkout action: this fetches the code from the repo calling the workflow
 - The style guide action: this fetches the styles and, if not present, a default config for Vale. The example fetches from the main branch since rules are currently under active development.
 - The vale/reviewdog action: this runs Vale using reviewdog, to insert comments into a pull-request

 This workflow uses reviewdog to insert output into review comments on any changes. The advantage of this method is:
  - the actions only run on new material (i.e. stuff added in the current PR)
  - it is surfaced directly where it will be noticed

[Vale styles]: https://vale.sh/docs/topics/styles/

## Running locally

There are times when it is useful to be able to manually run Vale from a terminal locally. The recommended way to do this is to clone the repository and then set up environment variables. Initially, you will need to create a local copy of the rules:

1. **Clone the repository**
   ```
   git clone https://github.com/canonical/documentation-style-guide.git
   ```
2. **Set environment variables**
   ```
   export VALE_CONFIG_PATH=~/documentation-style-guide/.vale.ini
   export VALE_STYLES_PATH=~/documentation-style-guide/styles
   ```
   Note: this assumes you cloned the repo directly to your home directory - adjust these paths if necessary.
3. **Confirm configuration**
   You can use built-in commands to check the configuration has been located and see the current paths:
   ```
   vale ls-config
   vale ls-vars
   ```

Now that Vale is installed you can check individual files or directories locally

```
vale docs
vale docs/*.md
vale docs/test.md
```

### Customising the rules

The published Vale GitHub action ignores suggestions and turns off some features which are likely to cause a lot of noise if run in their default state. A lot of things boil down to spellings. For example, the rule which checks for sentence case in headings doesn't know that SATA is an initialism by default, so if you include it, completely reasonably, in a heading it will be marked as an error. You may wish to turn this back on **if** you have a fairly complete vocabulary list.
The example `vale.ini` file enumerates all the current rules and explicitly sets their error levels. This makes it simple to turn rules on or off, or add the spelling options, by simply making a copy of this file, editing it and including it in the repository where the checks are run. 

## Documentation

The Style Guide documentation provides style guidance for technical documentation producded for Canonical products:

* [Canonical's documentation style guide](https://canonical-documentation-style-guide.readthedocs-hosted.com/)

### Building the documentation

The documentation can be built locally by running the following command from the `docs/` directory:

```
make run
```

If the build is successful, a local preview will be provided.

### Contributing to the documentation

When contributing changes to the documentation, please run the linting targets:

```
make spelling
make lint-md
make linkcheck
```

These checks are required for landing any changes to the documentation.
