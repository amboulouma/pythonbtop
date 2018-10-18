lst = [0, 1]
n = 0
while True:
    lst.append(lst[n] + lst[n+1])
    n += 1
    if len(lst) == 10:
        break
print(lst)
