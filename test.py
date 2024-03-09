items = [2, 104, 1]

diction = {}
sorted_items = sorted(items, reverse=True)

# 1st
if len(sorted_items) != 0:
    max_val = sorted_items.pop(0)
    diction[max_val] = "Gold Medal"

# 2nd
if len(sorted_items) != 0:
    max_val = sorted_items.pop(0)
    diction[max_val] = "Silver Medal"

# 3rd
if len(sorted_items) != 0:
    max_val = sorted_items.pop(0)
    diction[max_val] = "Bronze Medal"

for i, item in enumerate(sorted_items):
    diction[item] = str(i + 4)
result = [diction[item] for item in items]
print(result)
