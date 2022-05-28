# info.
# title: 입국심사
# algorith: binary search


def best_solution(n, times):
    """
        테스트 1 〉	통과 (0.01ms, 10.1MB)
        테스트 2 〉	통과 (0.19ms, 10MB)
        테스트 3 〉	통과 (3.58ms, 10.1MB)
        테스트 4 〉	통과 (270.12ms, 14.1MB)
        테스트 5 〉	통과 (503.25ms, 14.2MB)
        테스트 6 〉	통과 (307.21ms, 13.8MB)
        테스트 7 〉	통과 (512.98ms, 14.1MB)
        테스트 8 〉	통과 (631.07ms, 14.2MB)
        테스트 9 〉	통과 (0.03ms, 9.98MB)

    """
    answer = 0
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time
            # print(f"working: {mid // time} --> mid:{mid} , time: {time}")

        # print(f"mid:{mid} start:{start} end:{end} total: {total}")
        if total >= n:
            end = mid
        else:
            start = mid + 1

    answer = start
    return answer


test_cases = [

    (
        6, [7, 10],
        28
    ),
    (
        6, [7, 10, 3],
        12
    ),
    (
        6, [7, 10, 3, 4],
        9
    ),
    (
        6, [7, 10, 3, 4, 1],
        4
    ),
]

for i, test_case in enumerate(test_cases):

    n, times, answer = test_case

    solution = best_solution
    result = solution(n, times)

    assert answer == result, f"wrong answer in case [{i+1}] --> answer:{answer} / result: {result}"

    print(f"SUCCESS to pass case [{i+1}] !!\n")
