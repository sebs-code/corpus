import pytest
from decorators import do_twice

def test_do_twice():
    @do_twice
    def greet(name):
        return f"Hello, {name}!"

    result = greet("World")
    assert result == "Hello, World!"

def test_do_twice_with_side_effects():
    @do_twice
    def append_to_list(lst, item):
        lst.append(item)
        return lst

    my_list = []
    append_to_list(my_list, "item")
    assert my_list == ["item", "item"]

def test_do_twice_with_no_arguments():
    @do_twice
    def say_hello():
        return "Hello!"

    result = say_hello()
    assert result == "Hello!"

def test_do_twice_with_multiple_arguments():
    @do_twice
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

def test_do_twice_with_keyword_arguments():
    @do_twice
    def greet(name="World"):
        return f"Hello, {name}!"

    result = greet(name="Sebastian")
    assert result == "Hello, Sebastian!"

def test_do_twice_with_no_return():
    @do_twice
    def print_message(message):
        print(message)

    # This test is to ensure no exceptions are raised
    print_message("Hello, World!")

if __name__ == "__main__":
    pytest.main()