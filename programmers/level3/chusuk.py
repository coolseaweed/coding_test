
# info.
# title: [1차] 추석 트래픽

# 내 풀이
def solution(lines):
    """
        테스트 1 〉	통과 (0.02ms, 10.2MB)
        테스트 2 〉	통과 (62.85ms, 10.4MB)
        테스트 3 〉	통과 (59.41ms, 10.5MB)
        테스트 4 〉	통과 (0.01ms, 10.3MB)
        테스트 5 〉	통과 (0.44ms, 10.1MB)
        테스트 6 〉	통과 (0.45ms, 10.4MB)
        테스트 7 〉	통과 (62.89ms, 10.5MB)
        테스트 8 〉	통과 (63.01ms, 10.3MB)
        테스트 9 〉	통과 (0.74ms, 10.4MB)
        테스트 10 〉	통과 (0.02ms, 10.3MB)
        테스트 11 〉	통과 (0.02ms, 10.3MB)
        테스트 12 〉	통과 (63.10ms, 10.3MB)
        테스트 13 〉	통과 (0.47ms, 10.3MB)
        테스트 14 〉	통과 (0.01ms, 10.4MB)
        테스트 15 〉	통과 (0.01ms, 10.4MB)
        테스트 16 〉	통과 (0.01ms, 10.1MB)
        테스트 17 〉	통과 (0.01ms, 10.2MB)
        테스트 18 〉	통과 (180.03ms, 10.5MB)
        테스트 19 〉	통과 (249.08ms, 10.5MB)
        테스트 20 〉	통과 (252.53ms, 10.3MB)
        테스트 21 〉	통과 (0.00ms, 10.3MB)
        테스트 22 〉	통과 (0.01ms, 10.3MB)
    """
    answer = 0

    time_stamp_list = []
    for line in lines:
        date, time, ps = line.strip().split()
        ps = float(ps.replace("s", ""))
        hour, min, sec = time.split(":")
        end_sec = float(hour) * 3600 + float(min) * 60 + float(sec)

        start_sec = end_sec - ps + 0.001

        time_stamp_list.append((start_sec, end_sec))

    for i, time_stamp in enumerate(time_stamp_list):

        temp = 1
        start_sec, end_sec = time_stamp

        limit_start = end_sec
        limit_end = limit_start + 1

        for search_stamp in time_stamp_list[i+1:]:
            start_s_sec, end_s_sec = search_stamp

            # case 1
            # print(f"limit_start: {limit_start} / limit_end: {limit_end} / start_s_sec: {start_s_sec} / end_s_sec: {end_s_sec}")
            if limit_start < end_s_sec and end_s_sec < limit_end:
                # print("case 1")
                temp += 1
            elif start_s_sec < limit_start and end_s_sec < limit_end:
                # print("case 2")
                temp += 1

            elif start_s_sec > limit_start and end_s_sec > limit_end and start_s_sec < limit_end:
                # print("case 3")
                temp += 1
            elif start_s_sec < limit_start and end_s_sec > limit_end:
                # print("case 4")
                temp += 1

        if answer < temp:
            # print(f"answer is changed from {answer} -> {temp}")
            answer = temp

        # print(start_sec, end_sec, limit)
    return answer

# 베스트 정답


def best_solution(lines):
    """
        테스트 1 〉	통과 (0.02ms, 10.3MB)
        테스트 2 〉	통과 (3.19ms, 10.3MB)
        테스트 3 〉	통과 (1.75ms, 10.4MB)
        테스트 4 〉	통과 (0.01ms, 10.4MB)
        테스트 5 〉	통과 (0.29ms, 10.3MB)
        테스트 6 〉	통과 (0.15ms, 10.1MB)
        테스트 7 〉	통과 (1.55ms, 10.3MB)
        테스트 8 〉	통과 (1.53ms, 10.2MB)
        테스트 9 〉	통과 (0.30ms, 10.1MB)
        테스트 10 〉	통과 (0.02ms, 10.2MB)
        테스트 11 〉	통과 (0.05ms, 10.3MB)
        테스트 12 〉	통과 (2.11ms, 10.4MB)
        테스트 13 〉	통과 (0.15ms, 10.3MB)
        테스트 14 〉	통과 (0.01ms, 10.2MB)
        테스트 15 〉	통과 (0.01ms, 10.3MB)
        테스트 16 〉	통과 (0.01ms, 10.3MB)
        테스트 17 〉	통과 (0.01ms, 10.3MB)
        테스트 18 〉	통과 (3.08ms, 10.3MB)
        테스트 19 〉	통과 (3.13ms, 10.5MB)
        테스트 20 〉	통과 (3.10ms, 10.5MB)
        테스트 21 〉	통과 (0.01ms, 10.2MB)
        테스트 22 〉	통과 (0.01ms, 10.2MB)
    """
    # get input
    S, E = [], []
    totalLines = 0
    for line in lines:
        totalLines += 1
        type(line)
        (d, s, t) = line.split(" ")

       # time to float
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds - t + 0.001)

    # count the maxTraffic
    S.sort()

    curTraffic = 0
    maxTraffic = 0
    countE = 0
    countS = 0
    while((countE < totalLines) & (countS < totalLines)):
        if(S[countS] < E[countE]):
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1
        else:  # it means that a line is over.
            curTraffic -= 1
            countE += 1

    return maxTraffic


test_cases = [

    ([
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ],
        1
    ),
    (["2016-09-15 23:59:59.999 0.001s"],
        1

     ),
    (
        ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"],
        1
    ),
    (
        ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"],
        2
    ),
    (
        ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"],
        7
    ),
    (
        ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"], 1
    )
]

for i, test_case in enumerate(test_cases):
    input, answer = test_case
    result = solution(input)

    assert result == answer, f"wrong answer in case [{i+1}] // {input} result: {result} / answer: {answer} "

    print(f"SUCESS to pass case: {i+1}!!\n")
