from hello import hello
def test_hello_func():
    result = hello('gokul')
    assert result == 'hello gokul'

def test_hello_func2():
    result = hello('ganesh')
    assert result == 'hello gokul'