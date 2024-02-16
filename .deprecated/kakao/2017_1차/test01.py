
n = int(input('n='))
arr1 = list(map(int,input('arr1=').split(',')))
arr2 = list(map(int,input('arr1=').split(',')))

result = []
for i in range(n):
    binary = format(arr1[i]|arr2[i],'b')
    temp = ["#" if bit == '1' else ' ' for bit in binary ]
    result.append(''.join(temp))

print(result)
