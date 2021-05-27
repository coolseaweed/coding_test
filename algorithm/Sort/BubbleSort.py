def bubbleSort(list):
    n = 0

    for i in range(len(list)-1,0,-1):
        for idx in range(i):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
            n += 1
    print('-------------------------------------')
    print(f'\nbubble sort iterate num is [ {n} ] in [ {len(list)} ] length list\n')
    print('-------------------------------------')



def insertionSort(list):
    n = 0
    for i in range(1, len(list)):
        j = i - 1
        next_e = list[i]

        while (list[j] > next_e) and (j>=0):
            list[j+1] = list[j]
            j = j-1
            n += 1
        list[j+1] = next_e
        #print(list)

    print('-------------------------------------')
    print(f'\nInsertion sort iterate num is [ {n} ] in [ {len(list)} ] length list\n')
    print('-------------------------------------')


def mergeSort(num_list):
    n = 0
    if len(num_list) <= 1: return num_list

    mid = len(num_list)//2
    left_list = num_list[:mid]
    right_list = num_list[mid:]

    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)
    return merge(left_list,right_list)

def merge(left_list, right_list):
    res = []

    while len(left_list) !=0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        else:
            res.append(right_list[0])
            right_list.remove(right_list[0]) 

    if len(left_list) == 0:
        res += right_list
    else:
        res += left_list
    return res


def selectionSort(num_list):
    n = 0
    for idx in range(len(num_list)):
        min_idx = idx
        for j in range(idx+1, len(num_list)):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
            n += 1
        num_list[idx], num_list[min_idx] = num_list[min_idx], num_list[idx]


    print('-------------------------------------')
    print(f'\nselectionSort sort iterate num is [ {n} ] in [ {len(num_list)} ] length list\n')
    print('-------------------------------------')



list = [19,2,31,45,6,11,121,27,23,39,48,1,3]
print('target is :',list)
#bubbleSort(list)
#insertionSort(list)
# list  = mergeSort(list)
selectionSort(list)
print('sorted is :',list)
