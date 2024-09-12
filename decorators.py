# In Python, functions are first class objects (i.e. functions can be passed into other function). They can also return
# another function.

import functools


def do_twice(func):
    """
    Example of a simple decorator.
    """

    # We use this so that introspection matches the function being passed in.
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice
