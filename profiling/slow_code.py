# Running pytest with duration:
#   uv run pytest -vv --durations=0 profiling/slow_code.py
# reveals that test_inserting_10000_keys_reversed is much, much slower than other tests
# why? find the culprit using selected profiler AND *fix it.

import bisect
import unittest
from typing import Any, Iterator


class SortedDict:
    def __init__(self) -> None:
        self._dict: dict[str, Any] = {}
        self._sorted_keys: list[str] = []

    def __setitem__(self, key: str, value: Any) -> None:
        self._dict[key] = value
        # Find index to insert key so the order is maintained
        index = bisect.bisect_left(self._sorted_keys, key)
        self._sorted_keys.insert(index, key)

    def __getitem__(self, item: str) -> Any:
        return self._dict[item]

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        return ((key, self._dict[key]) for key in self._sorted_keys)


class TestSortedDict(unittest.TestCase):
    def test_iterates_in_sorted_value(self) -> None:
        sorted_dict = SortedDict()
        sorted_dict["b"] = 1
        sorted_dict["a"] = 3

        sorted_pairs = list(sorted_dict)
        self.assertEqual(sorted_pairs, [("a", 3), ("b", 1)])

    def test_inserting_10000_keys(self) -> None:
        sorted_dict = SortedDict()

        for key_as_int in range(10001, 20001):
            key = str(key_as_int)
            sorted_dict[key] = key_as_int

        self.assertEqual(len(list(sorted_dict)), 10000)

    def test_inserting_10000_keys_reversed(self) -> None:
        sorted_dict = SortedDict()

        for key_as_int in range(20001, 10001, -1):
            key = str(key_as_int)
            sorted_dict[key] = key_as_int

        self.assertEqual(len(list(sorted_dict)), 10000)


if __name__ == "__main__":
    unittest.main()
