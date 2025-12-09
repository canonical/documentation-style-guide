"""Tests for configuration in vale.ini"""

import pytest
import textwrap

# Data

def colon_fence_opening():
    """Case with starting fence with arbitrary directive."""

    return textwrap.dedent(
        """
        :::{lorem} ipsum
        """
    )

def colon_fence_code():
    """Case with colon-fenced `code` directive."""

    return textwrap.dedent(
        """
        :::{code}
        lorem
        :::
        """
    )

def colon_fence_code_block():
    """Case with colon-fenced `code-block` directive."""

    return textwrap.dedent(
        """
        :::{code-block}
        lorem
        :::
        """
    )

def colon_fence_sourcecode():
    """Case with colon-fenced `sourcecode` directive."""

    return textwrap.dedent(
        """
        :::{sourcecode}
        lorem
        :::
        """
    )

def colon_fence_terminal():
    """Case with colon-fenced `terminal` directive."""

    return textwrap.dedent(
        """
        :::{terminal}
        lorem
        :::
        """
    )

def colon_fence_toctree():
    """Case with colon-fenced `toctree` directive."""

    return textwrap.dedent(
        """
        :::{toctree}
        lorem
        :::
        """
    )

def colon_fence_parameter_options():
    """Case with a colon-fenced literal containing space and a parameter."""

    return textwrap.dedent(
        """
        ::: {code} python
        :number-lines:

        lorem
        :::
        """
    )

def colon_fence_serial():
    """Case with two colon-fenced literal directives separated by another block."""

    return textwrap.dedent(
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

def colon_fence_final_spaces():
    """Case with a colon-fenced literal directive with spaces after the closing
    fence."""

    return textwrap.dedent(
        """
        :::{code}
        lorem
        :::    
        """
    )

def colon_fence_special_chars():
    """Case with a colon-fenced literal containing all special characters."""

    return textwrap.dedent(
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
        \
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

def colon_fence_colons():
    """Case with a colon-fenced literal directive containing unescaped colons."""

    return textwrap.dedent(
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

def colon_fence_multiple():
    """Case with a literal directive fenced with more than three colons."""

    return textwrap.dedent(
        """
        ::::{code}
        lorem
        ::::
        """
    )

def colon_fence_nested():
    """Case with a colon-fenced non-literal directive containing:

    - A child that is a colon-fenced literal directive.
    - A child that is a colon-fenced non-literal directive."""

    return textwrap.dedent(
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

# Tests

@pytest.mark.parametrize(
    "run_vale_pipe_md, expected",
    [
        pytest.param(colon_fence_opening(), 0, id=colon_fence_opening.__name__),
        pytest.param(colon_fence_code(), 0, id=colon_fence_code.__name__),
        pytest.param(colon_fence_code_block(), 0, id=colon_fence_code_block.__name__),
        pytest.param(colon_fence_sourcecode(), 0, id=colon_fence_sourcecode.__name__),
        pytest.param(colon_fence_terminal(), 0, id=colon_fence_terminal.__name__),
        pytest.param(colon_fence_toctree(), 0, id=colon_fence_toctree.__name__),
        pytest.param(colon_fence_parameter_options(), 0, id=colon_fence_parameter_options.__name__),
        pytest.param(colon_fence_serial(), 0, id=colon_fence_serial.__name__),
        pytest.param(colon_fence_final_spaces(), 0, id=colon_fence_final_spaces.__name__),
        pytest.param(colon_fence_special_chars(), 0, id=colon_fence_special_chars.__name__),
        pytest.param(colon_fence_colons(), 0, id=colon_fence_colons.__name__),
        pytest.param(colon_fence_multiple(), 0, id=colon_fence_multiple.__name__),
        pytest.param(colon_fence_nested(), 0, id=colon_fence_nested.__name__),
    ],
    indirect=["run_vale_pipe_md"],
)
def test_markdown_blockignores(run_vale_pipe_md, expected):
    assert run_vale_pipe_md.returncode == expected
