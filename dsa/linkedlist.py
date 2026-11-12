"""Linked list problems: reverse, cycle detection, middle node."""


class ListNode:
    """Singly linked list node."""

    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        values = []
        node = self
        while node:
            values.append(str(node.val))
            node = node.next
        return "ListNode(" + " -> ".join(values) + ")"


def from_list(values):
    """Build a linked list from an iterable of values; returns the head."""
    head = tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head):
    """Collect linked list values into a Python list."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def reverse_linked_list(head):
    """Reverse a singly linked list iteratively.

    LeetCode 206. O(n) time, O(1) space.
    """
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


def has_cycle(head):
    """Detect a cycle with Floyd's tortoise-and-hare algorithm.

    LeetCode 141. O(n) time, O(1) space.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def middle_node(head):
    """Return the middle node (second middle when the length is even).

    LeetCode 876. O(n) time, O(1) space.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
