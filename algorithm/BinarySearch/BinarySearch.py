


def bSearch(num_list, key):
   
   # num_list must be sorted
    start = 0
    end = len(num_list) -1

    while start <= end:
        mid = (start + end)//2

        if num_list[mid] == key:
            return mid
        
        if key > num_list[mid]:
            start = mid+1
        else:
            end = mid-1
    
    if start > end: return None


def recursive_bSearch(num_list, start, end, key):

    if start > end: 
        return None
    
    else : 
        mid = (start + end)//2
        if num_list[mid] > key: return recursive_bSearch(num_list,start, mid-1, key)

        elif num_list[mid] < key: return recursive_bSearch(num_list,mid+1, end, key)

        else: return mid




test_list = [3,5,12,1,2,28,19]
test_list = sorted(test_list)
print(test_list)

print('\n\n######### here is bSearch ############')
print(bSearch(test_list,3))
print(bSearch(test_list,19))
print(bSearch(test_list,18))

print('\n\n######### here is recursive bSearch ############')
print(recursive_bSearch(test_list,0, len(test_list)-1,3))
print(recursive_bSearch(test_list,0, len(test_list)-1,19))
print(recursive_bSearch(test_list,0, len(test_list)-1,18))
