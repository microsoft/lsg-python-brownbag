"""List (and other) comprehensions are awesome!

All Python developers should familiarize themselves with
comprehensions and Python's built-in functions:
https://docs.python.org/3/library/functions.html

Functional programmers will want to look at the itertools module,
which implements a number of familiar constructs:
https://docs.python.org/3/library/itertools.html#itertools-recipes

However, many FP patterns can be written more clearly by taking
advantage of comprehensions.

"""


def test_generator_expression() -> None:
    """Underneath list comprehensions are generator expressions.

    Where `[i*i for i in range(10)]` is easily recognized as a 'list
    comprehension', the expression within the square brackets, or just
    `i*i for i in range(10)` is a generator expression.

    Python developers should get in the habit of preferring generator
    expressions over list comprehensions as they're generally
    efficient in terms of both memory and time.

    """
    # DONT do this! It’s an anti-pattern. Making the list is entirely
    # unnecessary and will take more memory.
    assert sum([i * i for i in range(10)]) == 285

    # OKAY do this instead! The expression returns an iterator which
    # lazily yields the values as needed by `sum` instead.
    assert sum(i * i for i in range(10)) == 285


def test_filtered_list() -> None:
    """We can filter using a comprehension and not a function.

    Functional programmers might drop straight to the use of
    `filter()` to apply a predicate to a list (or other iterable), but
    comprehensions support `if` and are more readable.

    https://docs.python.org/3/library/functions.html#filter

    """
    items = ["Foo", "Bar", "Baz"]
    filter_comprehension = [i for i in items if i.startswith("B")]
    filter_function = filter(lambda i: i.startswith("B"), items)
    assert filter_comprehension == list(filter_function)


def test_modified_list() -> None:
    """We can map logic onto items using a comprehension too.

    This replaces the built-in `map()` operator.

    https://docs.python.org/3/library/functions.html#map

    """
    items = ["Foo", "Bar", "Baz"]
    assert [i.lower() for i in items] == ["foo", "bar", "baz"]


def test_dict_comprehension() -> None:
    """Dictionaries can be made with comprehensions too.

    Sorry about this example being rather contrived. By the way, sets
    can also be created with comprehensions.

    """
    items = {i: f"i is {i}" for i in range(3)}
    assert list(items.keys()) == [0, 1, 2]
    assert items == {0: "i is 0", 1: "i is 1", 2: "i is 2"}
