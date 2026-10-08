"""Task 1: Two Sum Problem.

Find indices of two numbers in an array that add up to a target sum using a hash map.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional


def two_sum(numbers: list[int], target: int) -> Optional[list[int]]:
    """Find indices of two numbers that add up to target.

    Args:
        numbers: List of integers to search.
        target: Target sum.

    Returns:
        List containing indices of the two matching numbers [index1, index2],
        or None if no matching pair exists.
    """
    seen: dict[int, int] = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index
    return None


def run_demo() -> None:
    """Run demonstration test cases for Task 1."""
    print("=" * 40)
    print("TASK 1: TWO SUM PROBLEM DEMO")
    print("=" * 40)

    test_cases = [
        ([2, 7, 11, 15], 9, "Standard case"),
        ([3, 3], 6, "Duplicate numbers case"),
        ([3, 2, 4], 6, "Unsorted array case"),
        ([-1, -2, -3, -4, -5], -8, "Negative numbers case"),
        ([1, 2, 3, 4], 10, "No solution case"),
    ]

    for numbers, target, description in test_cases:
        result = two_sum(numbers, target)
        print(f"Description : {description}")
        print(f"Input       : numbers = {numbers}, target = {target}")
        print(f"Output      : {result}")
        if result is not None:
            i, j = result
            print(f"Verification: {numbers[i]} + {numbers[j]} = {numbers[i] + numbers[j]}")
        else:
            print("Verification: No matching pair found")
        print("-" * 40)


if __name__ == "__main__":
    run_demo()
