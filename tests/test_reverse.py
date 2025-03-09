from pathlib import Path
from src.reverse import reverse

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverce():
    before_string = read_file('before.txt')
    expected = read_file('result.txt')
    actual = reverse(before_string)

    assert actual == expected
