


def search_id(id,lists):
    for index in range(len(lists)):
        if lists[index]['id']==id:
            return lists[index]['name']



def solution(record):

    answer = []
    history = []
    user_list = []

    # checking same id in history and appending
    for index in range(len(record)):

        temp = record[index].split(" ")
        history.append(temp)

        same_id_check = False

        for v in range(len(user_list)):

            if user_list[v]['id']==temp[1]:

                try:
                    user_list[v]['name'] = temp[2]
                    same_id_check = True

                except IndexError:
                    same_id_check = True
                    continue
    
        if not same_id_check :
            user_list.append({'id':temp[1], 'name':temp[2]})
 

    # creating answer sheet    
    for index in range(len(history)):
        name = search_id(history[index][1],user_list)
        if history[index][0]=='Enter':
            answer.append(name+'님이 들어왔습니다.')
        elif history[index][0]=='Leave':
            answer.append(name+'님이 나갔습니다.')

    return answer



record = [
    "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
    "Enter uid1234 Prodo", "Change uid4567 Ryan", "Leave uid4567",
    "Change uid4567 Mola", "Enter uid4567 Colla"
    ]

answer = solution(record)

print(answer)





