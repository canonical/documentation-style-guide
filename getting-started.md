# Introduction to Vale rule development

The goal of this guide is to curate existing resources and provide pointers for anyone who is new to Vale rules. While it is not an in-depth tutorial, it aims to help you through installing and understanding Vale enough to create your first rules.

## Overview
* [Install the Vale CLI tool](#install-the-vale-cli-tool)
* [Develop a rule](#develop-a-rule)
  * [Basics](#basics)
* [Regex](#regex)
* [Test rules](#test-rules)
  * [Test all rules](#test-all-rules)
  * [Test a specific rule](#test-a-specific-rule)
* [Troubleshooting](#troubleshooting)


## Install the Vale CLI tool

The Vale CLI tool is the software that can apply Vale rules on any file in your local environment. This is how you can test your rule's behaviour while you develop it.

To install the Vale CLI tool, see the [installation guide](https://vale.sh/docs/vale-cli/installation/). To summarize:

- **For Windows and MacOS**, the easiest option is through the [package managers](https://vale.sh/docs/vale-cli/installation/#package-managers).

- **For Linux**, the easiest option depends on whether or not you have Docker (run `docker -v` to check if Docker is installed).
  * If you do, then you just have to [pull the container](https://vale.sh/docs/vale-cli/installation/#docker).
  * If you **don't**, the best option is to download the binaries from [Vale's GitHub releases](https://vale.sh/docs/vale-cli/installation/#github-releases). Installing Docker just for Vale is not worth the hassle.

## Develop a rule

A Vale rule is more than just a declaration or requirement - it's a definition of which lexical pattern(s) to search for and what to do when they are found. 

Vale has its own key/value convention for defining these rule parameters via YAML syntax. This section will go over some basic examples to understand the general structure of a rule, and resources for developing more complex ones.

### Basics

To develop a rule, you don't have to worry about setting up a particular environment or `vale.ini` configuration - all you need is an editor and this repository.

First, clone the repository if you haven't already.

```shell
git clone git@github.com:canonical/documentation-style-guide.git
```

Each rule is one file in the `styles/Canonical` directory. To create a new rule, add a `.yml` file and name it according to the convention you see in the other files: `000-Subject-brief-description.yml`.

> [!IMPORTANT]
> Vale rules only work with the extension **`.yml`**. They will not work with `.yaml`.

Here is an example of a simple rule that prints a message whenever it finds the words "gonna" and "gotta":

```yaml
extends: existence
message: "Do not use the contraction '%s'"
level: warning
tokens:
  - gonna
  - gotta
```

The **`extends`** key defines the type of search to perform. This is called an "[extension point](https://vale.sh/docs/topics/styles/#extension-points)".

The extension value '`existence`' checks whether certain words or characters exist. These are known as "[tokens](https://en.wikipedia.org/wiki/Lexical_analysis#Lexical_token_and_lexical_tokenization)". If a match is found, Vale will throw a warning and return our message.

A similar extension point is '`substitution`', but this one lets you define an alternative word to suggest to the user. For this extension point, you would use the **`swap`** key instead to map your tokens in the form of `wrong: right`, like in [this example](https://vale.sh/docs/topics/styles/#substitution).

There are several other extensions, each with a particular set of keys to fine-tune the logic of the search and the rule's reaction to a match.

You can now use the [documentation](https://vale.sh/docs/topics/styles/#extension-points) to find the extension point that best suits your rule, and see what parameters it requires.

### Resources

* Rule examples: 
  * [github.com/testthedocs](https://github.com/testthedocs/vale-styles/tree/master/ttd-light)
  * [github.com/errata-ai/vale](https://github.com/errata-ai/vale/tree/v3/testdata/styles)

* Documentation:
  * In general, the two most useful pages from the official Vale documentation for rule development are the [Styles](https://vale.sh/docs/topics/styles/) and [Scoping](https://vale.sh/docs/topics/scoping/) references.

## Regex

Sometimes you'll need to search for specific patterns, expressions, or symbols instead of single words. This is where regular expressions come in.

For example, to search for the expression "Not only ...but also", you can define a token that will capture this regardless of what is written in between. 

```yaml
tokens:
  - 'not only.*?but also'
```

The single quotes indicate the beginning and end of the regex, and the `.*?` quantifier indicates that any characters can be in between when looking for matches.


### Resources

- [Interactive regex tutorial](https://regexone.com/): Great for beginners
- [Regex editor](https://regex101.com/): Online tool that helps you compose and test your expressions. I like how it highlights capture groups in different colors.
- Before composing a complicated regex, remember to check for [existing rules](#resources) that might have done this already. 

## Test rules

Create a file in the root directory of the repository and fill it with text that you expect your rule to catch. It can be in any text format (`.txt`, `.md`, `.rst`...)

Besides the text file, the `vale` command needs a `vale.ini` config file. This file already exists in the root folder `documentation-style-guide/`. Vale will automatically find the `vale.ini` if you run the command in the same directory.

### Test all rules

To apply all the rules inside `styles/Canonical` at the same time, run `vale <file>` in the root directory `documentation-style-guide/`.

For example:

```shell
vale test.md
```

### Test a specific rule

To limit the test to a specific rule, you have to modify the `vale.ini` config file's [style specification](https://vale.sh/docs/topics/config/#basedonstyles).

The default config specifies `BasedOnStyles = Canonical`, which will test all rules in that folder.

Comment that line out and add a line enabling your rule using the syntax `<style>.<rule> = <YES | NO>`

This edit would look similar to the snippet below:

```ini
; BasedOnStyles = Canonical
Canonical.000-My-Rule = YES
```

Once it is saved, you can run the command `vale <file>` in the root directory `documentation-style-guide/`.

For example:

```shell
vale test.md
```

in the root directory `documentation-style-guide/`.

### Resources

* [Configuration documentation](https://vale.sh/docs/topics/config/#basedonstyles) -  make your own `vale.ini` file(s) with specific configs for your tests
* Run `vale -h` to see optional parameters like output style and config path.

## Troubleshooting

**My rule isn't getting applied to the text**
* Make sure the rule file uses the extension `.yml` instead of `.yaml`
* There might be a hidden syntax issue - consider using a local YAML linter or [online tool](https://jsonformatter.org/yaml-validator) to validate your rule.

### Conditionally ignoring rules

Some rules can be ignored conditionally, these conditions can come in a variety
of forms.

Rulesets that extend the default `existence` rule can use the dictionary to
ignore specific terms (including hyphenated terms or terms consisting of
multiple words).
