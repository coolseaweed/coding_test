from itertools import combinations



def solution01(relation):
    answer_list = []

    print(len(relation[0])) #attribute
    print(len(relation))    #rows


    for i in range(1,1<<len(relation[0])):

        temp_set = set()

        for j in range(len(relation)):
            temp = ''
            for k in range(len(relation[0])):
                if i & (1<<k):
                    temp += str(relation[j][k])
            temp_set.add(temp)

        if len(temp_set) == len(relation):
            is_Unique = True

            for num in answer_list:
                if (num & i) == num:
                    is_Unique = False
                    print(temp_set)

                    break
            
            if is_Unique:
                answer_list.append(i)

    return len(answer_list)


def solution02(relation):

    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col + 1):
        combination_i = combinations(range(n_col),i)
        candidates.extend(combination_i)
        # append 를 사용하게 될 경우 itertool 함수가 list 에 추가 된다. 
        # append 는 object 를 추가하는 것이고 extend 는 iterable object 의 element 를 추가하는 것이다. *중요

    n_row = len(relation)
    final = []
    for keys in candidates:
        temp = []
        for item in relation:
            a = []

            for key in keys:
                a.append(item[key])
            temp.append(tuple(a))
     #   print(temp)

        if len(set(temp)) == n_row:
            final.append(keys)

    answer = set(final)
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if set(final[i]) == set(final[i]).intersection(set(final[j])):
                answer.discard(final[j])


    return len(answer)


# this is my solution even didn't get close to answet though.. :(

def solution03(relation):

    index_list=[]
    num_attribute = len(relation[0])

    for i in range(num_attribute):
        index_list.append(i)

    powerset = get_powerset(index_list)

    unique_powerset = get_uniquness(relation,powerset)


def get_powerset(target_list):

    list_size = len(target_list)
    list_pow = []

    for i in range(2**list_size):
        flag = bin(i)[2:].zfill(list_size)
        subset = [target_list[j] for j in range(list_size) if flag[j]=='1']
        if subset==[] :
            continue
        else:
            list_pow.append(subset)

    return list_pow

def get_uniquness(relation,powerset):
    
    unique_powerset=[]
    for attributes in powerset:

        temp = []

        for i in range(len(relation)):
            key = None
            for v in attributes:
                if key == None:
                    key = relation[i][v]
                else :
                    key += relation[i][v]
            temp.append(key)


        if len(temp) == len(set(temp)):
            unique_powerset.append(attributes)
    return unique_powerset


relation = [
    ['100','ryan','music','2'], ['200','apeach','math','2'], ['300','tube','computer','3'],
    ['400','con','computer','4'], ['500','muzi', 'music', '3'], ['600', 'apeach', 'music', '2']
    ]


answer  = solution03(relation)


#print(answer)