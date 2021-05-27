def solution01(food_times, k):


    time = 0
    num_dish = len(food_times)

    if sum(food_times) <= k:
        return -1

    while sum(food_times) > 0:

        temp = time

        check = True

        while check:
            index = temp % num_dish    
            
            if food_times[index] - 1 < 0:
                temp += 1
            else:
                if time == k:
                    return index+1
                else :

                    food_times[index] -= 1
                    check = False

    
        time += 1
    
    



def solution02(food_times,k):
    answer = 0
    s_times = sorted(food_times)
    l_times = len(food_times)
    d_time = 0
    l_idx = 0
    
    for idx in range(l_times):

        if idx == 0:
            d_time += s_times[idx]*(l_times - idx)
        else :
            d_time += (s_times[idx]-s_times[idx-1])*(l_times-idx)
        
        if d_time > k:
            l_idx = idx -1
            break
    
    if d_time <= k :
        return -1
    
    lst = []
    for idx in range(l_times-1, -1, -1):
        if food_times[idx]>s_times[l_idx]:
            lst.append(idx+1)

    if len(lst) != 0:
        return lst[(d_time-k-1)%len(lst)]
    else:
        return (k)%l_times+1



food_times = [3,1,2]
k = 4


answer = solution01(food_times, k)
print(answer)
answer = solution02(food_times, k)
print(answer)
