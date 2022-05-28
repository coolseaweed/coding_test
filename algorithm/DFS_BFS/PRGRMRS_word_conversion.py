# info.
# title: 단어 변환
# level: 3
# category: BFS & DFS

from collections import deque


def get_word_diff(word1, word2):

    count = 0
    if len(word1) != len(word2):
        return count

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return count


def solution(begin, target, words):
    """
        테스트 1 〉	통과 (0.01ms, 10.1MB)
        테스트 2 〉	통과 (0.09ms, 10MB)
        테스트 3 〉	통과 (0.46ms, 10.2MB)
        테스트 4 〉	통과 (0.02ms, 10.2MB)
        테스트 5 〉	통과 (0.00ms, 10.1MB)
    """
    answer = 0

    visited = {begin: 0}

    queue = deque([begin])

    while queue:

        curr = queue.popleft()
        # print(f"curr: {curr}")
        # print(f"queue: {queue}")
        # print(f"visited: {visited}")
        # print("-----------------------")

        for word in words:
            if word in visited:
                continue

            if get_word_diff(word, curr) == 1:
                visited[word] = visited[curr] + 1
                queue.append(word)

    return visited.get(target, 0)


test_cases = [

    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0)

]


for i, test_case in enumerate(test_cases):

    begin, target, words, answer = test_case

    result = solution(begin, target, words)

    assert answer == result, f"wrong answer case [{i+1}] --> answer:{answer} result:{result}"

    print(f"SUCCESS to pass test case [{i+1}]")
