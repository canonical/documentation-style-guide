"""Tests for configuration in vale.ini"""

import textwrap


def test_colon_fence_arbitrary(test_markdown):
    """Case with starting fence with arbitrary directive."""

    test_markdown(
        textwrap.dedent(
            """
            :::{lorem} ipsum
            """
        )
    )


def test_colon_fence_code(test_markdown):
    """Case with colon-fenced `code` directive."""

    test_markdown(
        textwrap.dedent(
            """
            :::{code}
            lorem
            :::
            """
        )
    )


def test_colon_fence_code_block(test_markdown):
    """Case with colon-fenced `code-block` directive."""

    test_markdown(
        textwrap.dedent(
            """
            :::{code-block}
            lorem
            :::
            """
        )
    )


def test_colon_fence_sourcecode(test_markdown):
    """Case with colon-fenced `sourcecode` directive."""

    test_markdown(
        textwrap.dedent(
            """
            :::{sourcecode}
            lorem
            :::
            """
        )
    )


def test_colon_fence_terminal(test_markdown):
    """Case with colon-fenced `terminal` directive."""

    test_markdown(
        textwrap.dedent(
            """
            :::{terminal}
            lorem
            :::
            """
        )
    )


def test_colon_fence_toctree(test_markdown):
    """Case with colon-fenced `toctree` directive."""

    test_markdown(
        textwrap.dedent(
            """
            :::{toctree}
            lorem
            :::
            """
        )
    )


def test_colon_fence_parameter_options(test_markdown):
    """Case with a colon-fenced literal containing space and a parameter."""

    test_markdown(
        textwrap.dedent(
            """
            ::: {code} python
            :number-lines:

            lorem
            :::
            """
        )
    )


def test_colon_fence_serial(test_markdown):
    """Case with two colon-fenced literal directives separated by another block."""

    test_markdown(
        textwrap.dedent(
            """
            :::{code}
            lorem
            :::

            Break.

            :::{code}
            ipsum
            :::
            """
        )
    )


def test_colon_fence_final_spaces(test_markdown):
    """Case with a colon-fenced literal directive with spaces after the closing
    fence."""

    test_markdown(
        textwrap.dedent(
            """
            :::{code}
            lorem
            :::    
            """
        )
    )


def test_colon_fence_special_chars(test_markdown):
    """Case with a colon-fenced literal containing all special characters."""

    test_markdown(
        textwrap.dedent(
            """
            :::{code}
            `~!@#$%^&&*()-=_+[]{}\\|;':",./<>?
            ~
            !
            @
            #
            $
            %
            ^
            &
            *
            (
            )
            -
            =
            _
            +
            [
            ]
            {
            }
            \\
            |
            ;
            '
            :
            "
            ,
            .
            /
            <
            >
            ?
            :::
            """
        )
    )


def test_colon_fence_colons(test_markdown):
    """Case with a colon-fenced literal directive containing unescaped colons."""

    test_markdown(
        textwrap.dedent(
            """
            :::{code}
            :
            ::

            ::
            :
            ::

            :::
            """
        )
    )


def test_colon_fence_multiple(test_markdown):
    """Case with a literal directive fenced with more than three colons."""

    test_markdown(
        textwrap.dedent(
            """
            ::::{code}
            lorem
            ::::
            """
        )
    )


def test_colon_fence_nested(test_markdown):
    """Case with a colon-fenced non-literal directive containing:

    - A child that is a colon-fenced literal directive.
    - A child that is a colon-fenced non-literal directive."""

    test_markdown(
        textwrap.dedent(
            """
            ::::{admonition} Level 1

            :::{code}
            lorem
            :::

            :::{admonition} Level 2
            Hello, world!
            :::

            ::::
            """
        )
    )
