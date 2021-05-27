
def mergeSort(num_list):

    if len(num_list) <= 1: return num_list

    mid = len(num_list)//2

    left_list = num_list[:mid]
    right_list = num_list[mid:]

    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)

    return merge(left_list, right_list)

def merge(left_list, right_list):
    res = []
    
    while len(left_list) != 0 and len(right_list) != 0:

        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.pop(0)
        else:
            res.append(right_list[0])
            right_list.pop(0)
    
    if len(left_list) == 0:
        res += right_list
    else:
        res += left_list
    
    return res


num_list = [19,2,31,45,6,11,121,27,23,39,48,1,3]


sorted_list = mergeSort(num_list)

print(sorted_list)


