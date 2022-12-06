from gome_tests.func_get_val import get_val

def test_get_val():
    assert get_val({"hello": "world"}, "hello") == "world"


def test_get_val_two():
    assert get_val({"hello": "world"}, "hello", "python") == "world"


def test_get_val_three():    
    assert get_val({}, "hello", "python") == "python"
    
