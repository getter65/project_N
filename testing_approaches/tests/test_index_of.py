from testing_approaches.index_of import index_of

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([], 1) == -1
    assert index_of([1, 1, 1], 2) == -1
    assert index_of([1, 3, 4, 2], 4) == 2