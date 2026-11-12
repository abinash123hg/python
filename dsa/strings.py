"""String problems: longest unique-character substring, group anagrams, palindrome."""

from collections import defaultdict


def longest_unique_substring(s):
    """Return the length of the longest substring without repeating characters.

    LeetCode 3. Sliding window, O(n) time.
    """
    last_seen = {}
    start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best


def group_anagrams(strs):
    """Group words that are anagrams of each other.

    LeetCode 49. O(n * k log k) where k is the longest word length.
    """
    groups = defaultdict(list)
    for word in strs:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


def valid_palindrome(s):
    """Return True if s reads the same forward and backward, ignoring
    non-alphanumeric characters and case. LeetCode 125. Two pointers, O(n).
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
