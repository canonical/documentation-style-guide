"""Tests for configuration in vale.ini"""

import textwrap


def test_md_colon_fence_arbitrary(test_raw):
    """Case with starting fence with arbitrary directive."""

    test_raw(
        textwrap.dedent(
            """
            :::{lorem} ipsum
            """
        ),
        ".md",
    )


def test_md_colon_fence_code(test_raw):
    """Case with colon-fenced `code` directive."""

    test_raw(
        textwrap.dedent(
            """
            :::{code}
            lorem
            :::
            """
        ),
        ".md",
    )


def test_md_colon_fence_code_block(test_raw):
    """Case with colon-fenced `code-block` directive."""

    test_raw(
        textwrap.dedent(
            """
            :::{code-block}
            lorem
            :::
            """
        ),
        ".md",
    )


def test_md_colon_fence_sourcecode(test_raw):
    """Case with colon-fenced `sourcecode` directive."""

    test_raw(
        textwrap.dedent(
            """
            :::{sourcecode}
            lorem
            :::
            """
        ),
        ".md",
    )


def test_md_colon_fence_terminal(test_raw):
    """Case with colon-fenced `terminal` directive."""

    test_raw(
        textwrap.dedent(
            """
            :::{terminal}
            lorem
            :::
            """
        ),
        ".md",
    )


def test_md_colon_fence_toctree(test_raw):
    """Case with colon-fenced `toctree` directive."""

    test_raw(
        textwrap.dedent(
            """
            :::{toctree}
            lorem
            :::
            """
        ),
        ".md",
    )


def test_md_colon_fence_parameter_options(test_raw):
    """Case with a colon-fenced literal containing space and a parameter."""

    test_raw(
        textwrap.dedent(
            """
            ::: {code} python
            :number-lines:

            lorem
            :::
            """
        ),
        ".md",
    )


def test_md_colon_fence_serial(test_raw):
    """Case with two colon-fenced literal directives separated by another block."""

    test_raw(
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
        ),
        ".md",
    )


def test_md_colon_fence_final_spaces(test_raw):
    """Case with a colon-fenced literal directive with spaces after the closing
    fence."""

    test_raw(
        textwrap.dedent(
            """
            :::{code}
            lorem
            :::    
            """
        ),
        ".md",
    )


def test_md_colon_fence_special_chars(test_raw):
    """Case with a colon-fenced literal containing all special characters."""

    test_raw(
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
        ),
        ".md",
    )


def test_md_colon_fence_colons(test_raw):
    """Case with a colon-fenced literal directive containing unescaped colons."""

    test_raw(
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
        ),
        ".md",
    )


def test_md_colon_fence_multiple(test_raw):
    """Case with a literal directive fenced with more than three colons."""

    test_raw(
        textwrap.dedent(
            """
            ::::{code}
            lorem
            ::::
            """
        ),
        ".md",
    )


def test_md_colon_fence_nested(test_raw):
    """Case with a colon-fenced non-literal directive containing:

    - A child that is a colon-fenced literal directive.
    - A child that is a colon-fenced non-literal directive."""

    test_raw(
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
        ),
        ".md",
    )


def test_md_role_intersphinx_links(test_raw):
    """Case with links to Intersphinx project:

    - An external Intersphinx ref.
    - An external Intersphinx doc."""

    test_raw(
        textwrap.dedent(
            """
            {external:ref}`test`
            {external:py:class}`test`
            {external+launchpad:ref}`test`
            {external+launchpad:doc}`test`
            """
        ),
        ".md",
    )


def test_rst_role_intersphinx_links(test_raw):
    """Case with links to Intersphinx project:

    - An external Intersphinx ref.
    - An external Intersphinx doc."""

    test_raw(
        textwrap.dedent(
            """
            :external:ref:`test`
            :external:py:class:`test`
            :external+launchpad:ref:`test`
            :external+launchpad:doc:`test`
            """
        ),
        ".rst",
    )
