from func_get_val import get_val

def test_get_val(get_val):
    assert get_val({"hello": "world"}, "hello") == "world"
    assert get_val({"hello": "world"}, "hello", "python") == "world"
    assert get_val({}, "hello", "python") == "python"
    
test_get_val(get_val)
