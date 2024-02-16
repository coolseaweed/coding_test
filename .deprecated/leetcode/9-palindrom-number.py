def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    target = str(x)
    # print(f"len: {len(target)}")

    num = len(str(x)) // 2 + 1

    for i in range(num):
        if target[i] == target[-(i + 1)]:
            continue
        else:
            # print(f"[{i}] target[i]:{target[i]} != target[-(i+1)]:{target[-(i + 1)]}")
            return False

    return True


def main():
    test_cases = [(121, True), (-121, False), (10, False)]
    for test_case in test_cases:
        nums, expected = test_case
        assert isPalindrome(nums) == expected


if __name__ == "__main__":
    main()
