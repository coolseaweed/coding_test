

string = 'teeter'


table = {}
for c in string:
    print(c)
    if c not in table:
        table[c] = 1
    else:
        table[c] += 1
    print(table)
print('-----------------------')
for key,val in table.items():
    if val == 1:
        print(key)
        break
    