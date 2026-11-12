"""Array problems: two sum, maximum subarray, merge intervals."""


def two_sum(nums, target):
    """Return indices of the two numbers that add up to target.

    LeetCode 1. O(n) time, O(n) space.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("no two numbers add up to the target")


def maximum_subarray(nums):
    """Return the largest contiguous subarray sum (Kadane's algorithm).

    LeetCode 53. O(n) time, O(1) space.
    """
    best = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


def merge_intervals(intervals):
    """Merge all overlapping intervals, returned sorted by start.

    LeetCode 56. O(n log n) time.
    """
    if not intervals:
        return []
    ordered = sorted(intervals)
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
