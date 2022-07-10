arr = [1,0,2,3,0,4,5,0]
lst = []
for zero in arr:
    if len(lst) >= len(arr):
        break
    if zero == 0:
        lst.append(zero)
        lst.append(zero)
    else:
        lst.append(zero)

for i in range(len(arr)):
    arr[i] = lst[i]
print(arr)