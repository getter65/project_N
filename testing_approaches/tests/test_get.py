from testing_approaches.get import get

def test_get():
    assert get([1, 2, 3], 1, "a") == 2
    assert get([4, 5, 6], 7, "val") == "val"
    assert get([7, 8, 9], -1) == None