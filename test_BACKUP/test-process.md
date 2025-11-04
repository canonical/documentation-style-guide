# Test criteria

When writing tests for this suite, several considerations must be made


## Format support

Our Vale rules aim to support the source formats we use in documentation. This
means support for MD and RST file types is essential. In addition to this, we
want to support docstrings, and HTML.

In some cases, due to the different syntax used in these different files,
multiple test files are needed.

Rules should, by default, use both MD and RST test files. Any rules using the
'raw' scope also require a HTML test file.

## Test considerations

Each test should have minimal coverage for the intended purpose, with additional
test cases added for edge case syntax.

### Examples

For 400-Enforce-inclusive-terms, a large number of terms are stated for capture.
Not all these terms need to be included in a test file - but examples of terms
with different formatting should be included. For example, "man hours" and
"middleman" should be included in the tests as they include different non-word
characters (in this case, a space).

