"""This demonstrates Python's type annotations.

The Python typing library:
https://docs.python.org/3.8/library/typing.html

Mypy is the de facto static type checker:
http://mypy-lang.org/

And they have a type hints cheat sheet:
https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html

Dropbox added type checking to 4 million lines of Python:
https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python

PEP 563 (2007) explains why we use __future__.annotations:
https://www.python.org/dev/peps/pep-0563/

PEP 3107 (2006) introduced the function annotation syntax:
https://www.python.org/dev/peps/pep-3107/

PEP 484 (2014) is the introduction of type hints:
https://www.python.org/dev/peps/pep-0484/

PEP 526 (2016) introduced the variable annotation syntax:
https://www.python.org/dev/peps/pep-0526/

Until Python 3.10 is released, function and variable annotations are
evaluated at definition time. This means that any object used in an
annotation (like `typing.Optional`) needs to be imported at runtime,
despite not being used by anything else. Starting in Python 3.7, the
`__future__` module backports the new `annotations`, which allows
developers to only import types from `typing` when is being statically
type checked, instead of all the time, and this condition used for
this import is a simple boolean `typing.TYPE_CHECKING`.

"""

from __future__ import annotations

import typing

# This value is False at runtime but True to type checkers, like Mypy.
if typing.TYPE_CHECKING:
    from typing import Iterable, List, Optional, Set, Tuple


def greeting(name: Optional[str] = None) -> str:
    """Says hello given an optional name.

    NOTE: `Optional` is just a convenience. It's equivalent to
    `Union[str, None]`.

    """
    if name:
        return f"Hello {name}!"
    else:
        return "Hello you!"


def test_greeting() -> None:
    # DEMO: Default arguments and "Truthy" vs "Falsy" in Python.
    assert greeting() == "Hello you!"
    assert greeting(None) == "Hello you!"
    assert greeting("") == "Hello you!"

    # DEMO: Quick aside on f-string formatting!
    assert greeting("Andy") == "Hello Andy!"

    # DEMO: Type checking is static not runtime!
    assert greeting(42) == "Hello 42!"


def greetings(names: Iterable[str]) -> List[str]:
    """Says hello to an iterable of names.

    From PEP 484:

    NOTE: `Dict`, `List` and `Set` are mainly useful for annotating
    *return* values. For *arguments*, prefer abstract collection types
    `Iterable`, `Mapping`, `Sequence` or `AbstractSet`.

    """
    return [greeting(name) for name in names]


def test_greetings_list() -> None:
    expected: List[str] = ["Hello Alice!", "Hello Bob!"]
    # DEMO: Lists are Iterable.
    names_list: List[str] = ["Alice", "Bob"]
    assert greetings(names_list) == expected

    # DEMO: Tuples are Iterable.
    names_tuple: Tuple[str, str] = ("Alice", "Bob")
    assert greetings(names_tuple) == expected

    # DEMO: Sets are Iterable but not Sequences! The three basic
    # sequence types are list, tuple, and range (see above), but a
    # more generic concept of “things” is anything iterable.
    # https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
    names_set: Set[str] = {"Alice", "Bob"}
    # NOTE: We have to sort because Python sets are unordered.
    assert sorted(greetings(names_set)) == expected
