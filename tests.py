from typing import List

from main import get_first_time


def test():
    cur_time = "23:10"
    with open("test_config.txt") as f:
        results: List = get_first_time(cur_time, f)
        assert results[0] == "17:00 tomorrow - /bin/.."
        assert results[1] == "23:10 today - /bin/.."
        assert results[2] == "0:05 tomorrow - /bin/.."
        assert results[3] == "19:59 tomorrow - /bin/.."
        assert results[4] == "23:09 tomorrow - /bin/.."
