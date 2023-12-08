# Problem: https://www.hackerrank.com/challenges/py-the-captains-room

k = int(input())
arr = list(map(int, input().split()))

set_arr = set(arr)

for i in set_arr:
    temp = 0
    for x in arr:
        if x == i:
            temp += 1
            if temp == 2:
                break
    if temp == 1:
        print(i)
    else:
        temp = 0
