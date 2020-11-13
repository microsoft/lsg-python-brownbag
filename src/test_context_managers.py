"""Manage the lifetime of your resources wisely!

Use context managers for anything that needs automatic cleanup.

See this fantastic writeup:
https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

And the context manager documentation:
https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers

"""
from __future__ import annotations

import typing
from contextlib import contextmanager

import pytest

if typing.TYPE_CHECKING:
    from typing import IO, Any, Generator


class AManualContextManager:
    """Make a context manager manually.

    This is a contrived example because Python's built-in `open()` is
    already usable as a context manager, so we're wrapping it.

    """

    def __init__(self, name: str):
        self.open_file = open(name)

    def __enter__(self) -> IO[Any]:
        """Opens the context (enters the scope).

        https://docs.python.org/3/reference/datamodel.html#object.__enter__

        """
        return self.open_file

    def __exit__(self, type, value, traceback):  # type: ignore
        """Closes the context (exits the scope).

        https://docs.python.org/3/reference/datamodel.html#object.__exit__

        NOTE: I ignored the types here because I don't know them!

        """
        self.open_file.close()


def test_manager_class() -> None:
    """We can read within the context but not outside it."""
    with AManualContextManager("src/__init__.py") as f:
        # We can read it because it’s open.
        assert f.readline() == ""

    # This fails because the file has been automatically closed.
    with pytest.raises(ValueError):
        assert f.readline() == ""


@contextmanager
def a_manual_manager(name: str) -> Generator[IO[Any], None, None]:
    """Context managers can be made with 'yield' too."""
    open_file = open(name)
    yield open_file
    open_file.close()


def test_manager_function() -> None:
    """We can read within the context but not outside it."""
    with a_manual_manager("src/__init__.py") as f:
        # We can read it because it’s open.
        assert f.readline() == ""

    # This fails because the file has been automatically closed.
    with pytest.raises(ValueError):
        assert f.readline() == ""
