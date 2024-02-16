rom2int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    int_list = [rom2int[char] for char in s]
    print(int_list)
    result = 0
    prev = 0
    for i, num in enumerate(int_list):
        if i == 0:
            prev = num
            result += num
            continue

        if prev >= num:
            result += num
        else:
            result += num - prev

        prev = num

        print(f"i:{i} / num: {num} / result: {result}")


def main():
    test_cases = [("MCMXCIV", 1994), ("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]
    for test_case in test_cases:
        nums, expected = test_case
        assert romanToInt(nums) == expected


if __name__ == "__main__":
    main()
