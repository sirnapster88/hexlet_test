import sys
sys.path[0] = 'd:\study\hexlet_pytest'
from pathlib import Path
from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_process():
    test_data = read_file("normal_text.txt")
    expected = read_file("reverse_text.txt")
    actual = reverse(test_data)

    assert actual == expected