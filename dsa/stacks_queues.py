"""Stack and queue problems: balanced parentheses, min stack, LRU cache."""

from collections import OrderedDict


def valid_parentheses(s):
    """Return True if the bracket string is balanced.

    LeetCode 20. Stack, O(n) time.
    """
    closing = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in closing:
            if not stack or stack.pop() != closing[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


class MinStack:
    """Stack with O(1) push, pop, top and get_min. LeetCode 155."""

    def __init__(self):
        self._items = []
        self._mins = []

    def push(self, val):
        self._items.append(val)
        self._mins.append(min(val, self._mins[-1]) if self._mins else val)

    def pop(self):
        self._mins.pop()
        return self._items.pop()

    def top(self):
        return self._items[-1]

    def get_min(self):
        return self._mins[-1]


class LRUCache:
    """Least-recently-used cache with O(1) get and put. LeetCode 146."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._data = OrderedDict()

    def get(self, key):
        if key not in self._data:
            return -1
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key, value):
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self._capacity:
            self._data.popitem(last=False)
