"""This demonstrates Python's generators.

A generator function behaves like an iterator which means it can be
used in places like a for loop. While generators can be manually
implemented as a class with the expected methods `__iter__` (which
returns itself) and `__next__` (which returns the next element and
raises `StopIteration` when done), this pattern is common enough to
have its own keyword support in Python with `yield`.

Generators are really useful because they're lazy, and the best
programming is lazy programming! In this sense it means that the
values are generated on-demand instead of all at once. Compare the
pattern to producing a list of items and then using the list, versus
generating and using each item one at a time. Less memory!

Iterator types:
https://docs.python.org/3/library/stdtypes.html#typeiter

Yield expressions:
https://docs.python.org/3/reference/expressions.html#yieldexpr

PEP 255 (2001) defined simple generators:
https://www.python.org/dev/peps/pep-0255/

"""
from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from typing import Generator


class AManualIterator:
    """A manually implemented iterator which counts to a given limit.

    DONT do this! Use `yield` instead.

    """

    count: int
    limit: int

    def __init__(self, limit: int) -> None:
        """Initializes the iterator with a limit."""
        self.count = 0
        self.limit = limit

    def __iter__(self) -> "AManualIterator":
        """Returns the Iterator.

        This method is expected on all iterators.

        The Python built-in `iter(it)` calls `it.__iter__()`.
        (Ignoring built-in containers and creation of iterators.)

        NOTE: Type hints in Python have a forward declaration problem.
        The admittedly inelegant solution is to simply use strings for
        types which are not yet defined.

        """
        return self

    def __next__(self) -> int:
        """Returns the next value during iteration.

        This method is expected on all iterators.

        The Python built-in `next(it)` calls `it.__next__()`, as does
        the `for` keyword (though the details are more complicated.)

        """
        if self.count >= self.limit:
            raise StopIteration
        else:
            self.count += 1
            return self.count


def test_manual_iterator() -> None:
    """We can create a list from the iterated values."""
    assert [i for i in AManualIterator(3)] == [1, 2, 3]


def a_yield_iterator(limit: int) -> Generator[int, None, None]:
    """A much simpler version of the same thing.

    The `yield` keyword is like a scoped `return`. When a function
    yields, the state of the function (such as `count` and `limit`
    here) are saved and the value is returned (well, "yielded") to the
    caller. When the function is called again the state is restored
    and the next value is yielded.

    This is rather similar to the asynchronous concept of coroutines,
    since they have more than one entry point and their execution can
    be suspended, but control is always given back to the caller.

    """
    count = 0
    while count < limit:
        count += 1
        yield count


def test_yield_iterator() -> None:
    """The usage is identical to the manual iterator."""
    assert [i for i in a_yield_iterator(3)] == [1, 2, 3]
