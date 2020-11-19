import os

def test_one():
    expected = os.getenv("FOUR")
    if expected != None:
        expected = int(expected)
    else:
        expected = 4
    assert 2 + 2 == expected
