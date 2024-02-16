def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index, num in enumerate(nums):
        if target - num in nums[index + 1 :]:
            return [index, nums[index + 1 :].index(target - num) + index + 1]


def main():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for test_case in test_cases:
        nums, target, expected = test_case
        assert twoSum(nums, target) == expected


if __name__ == "__main__":
    main()
