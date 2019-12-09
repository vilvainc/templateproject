from src.templatemodule.hello import say_hello

def test_print_hello():
    assert say_hello() == "hello"
    assert not say_hello() is None