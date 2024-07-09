import pytest
from unique_characters import count_from_file, unique_characters
from unittest.mock import Mock, patch, mock_open
import os


@pytest.mark.parametrize("string, expected_result",
                         [('abbbccdf', 3),
                          ('xy', 2),
                          ('o', 1),
                          ('aaa', 0)
                          ])
def test_unique(string, expected_result):
    assert unique_characters(string) == expected_result


@pytest.mark.parametrize("exception, parameter",
                         [(ValueError, 23),
                          (TypeError, ['abbbccdf', 'xy', 'aaa']),
                          (TypeError, {1: 1, "2": 2})
                          ])
def test_not_str(exception, parameter):
    with pytest.raises(exception):
        unique_characters(parameter)


def test_cache():
    unique_characters.cache_clear()
    unique_characters('abbbccdf')
    unique_characters('abbbccdf')
    hits = list(unique_characters.cache_info())[0]
    assert hits == 1


def test_mock_count_file():
    mock = Mock()
    mock.unique_characters.return_value = 4
    file_path = os.path.join(os.path.dirname(__file__), '../text.txt')
    with patch('builtins.open', mock_open(read_data="jhffccvb")):
        actual = count_from_file(file_path)
    assert actual == mock.unique_characters.return_value


if __name__ == "__main__":
    pytest.main()
