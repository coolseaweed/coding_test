


def solution(N,stages):

    fail_rate = []
    num_people = len(stages)

    for stage_num in range(N):
        challenge_cnt = 0
        stage_arrive_cnt = 0

        for v in range(num_people):
            if stage_num + 1 == stages[v]:
                challenge_cnt += 1
            if stage_num < stages[v]:
                stage_arrive_cnt +=1


        fail_rate.append(challenge_cnt/stage_arrive_cnt)
        
    sort_data = sorted(range(len(fail_rate)), key=lambda k:fail_rate[k], reverse=True)

    for i in range(N):
        sort_data[i] +=1

    return sort_data


N = 5
stages = [2,1,2,6,2,4,3,3]

# N = 4
# stages = [4,4,4,4,4]


answer = solution(N,stages)

print(answer)