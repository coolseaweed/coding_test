# 문제 설명
# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
# 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
# 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.

# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
# 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
# 입출력 예
# citations	return
# [3, 0, 6, 1, 5]	3
# 입출력 예 설명
# 이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 
# 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

# ※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.


def my_solution(citations):

    num_papers = len(citations)
    answer = None
    for h in reversed(range(1,num_papers+1)):

        cnt_up = 0
        cnt_down = 0
        for i in citations:
            if h >= i:
                cnt_down += 1
            if h <= i:
                cnt_up +=1
            

        if (cnt_up >= h) and  (cnt_down <= h):
            answer = h
            return answer
            
    if answer == None:
        return 0

def better_solution(citations):

    sorted_list = sorted(citations)
    citation_size = len(citations)


    index = 0
    for i in range(len(citations)):
        h = citation_size - i

        if sorted_list[i] >= h:
            return h


citations = [
    [1,7,0,1,6,4],
    [3,0,6,1,5],    
    [0],
    [1642, 2, 999, 790, 540, 10, 22],
    [7],
    [6,6,6,6,6,6],
    [10,100],
    [10,50,100]
    ]

#answer = better_solution(citations[0])

for citation in citations:
    answer = better_solution(citation)

    print(answer)