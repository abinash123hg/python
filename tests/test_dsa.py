import unittest

from dsa.arrays import maximum_subarray, merge_intervals, two_sum
from dsa.linkedlist import (
    from_list,
    has_cycle,
    ListNode,
    middle_node,
    reverse_linked_list,
    to_list,
)
from dsa.stacks_queues import LRUCache, MinStack, valid_parentheses
from dsa.strings import group_anagrams, longest_unique_substring, valid_palindrome


class ArraysTest(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_maximum_subarray(self):
        self.assertEqual(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_merge_intervals(self):
        self.assertEqual(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
                         [[1, 6], [8, 10], [15, 18]])


class StringsTest(unittest.TestCase):
    def test_longest_unique_substring(self):
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(longest_unique_substring("bbbbb"), 1)

    def test_group_anagrams(self):
        groups = sorted(sorted(g) for g in group_anagrams(["eat", "tea", "bat"]))
        self.assertEqual(groups, [["bat"], ["eat", "tea"]])

    def test_valid_palindrome(self):
        self.assertTrue(valid_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(valid_palindrome("race a car"))


class LinkedListTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(to_list(reverse_linked_list(from_list([1, 2, 3]))), [3, 2, 1])

    def test_cycle_detection(self):
        head = from_list([1, 2, 3])
        self.assertFalse(has_cycle(head))
        tail = head.next.next
        tail.next = head.next
        self.assertTrue(has_cycle(head))

    def test_middle_node(self):
        self.assertEqual(middle_node(from_list([1, 2, 3, 4])).val, 3)


class StacksQueuesTest(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertTrue(valid_parentheses("({[]})"))
        self.assertFalse(valid_parentheses("([)]"))

    def test_min_stack(self):
        stack = MinStack()
        for value in [-2, 0, -3]:
            stack.push(value)
        self.assertEqual(stack.get_min(), -3)
        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.get_min(), -2)

    def test_lru_cache(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)


if __name__ == "__main__":
    unittest.main()
