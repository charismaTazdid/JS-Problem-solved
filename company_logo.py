# Problem: https://www.hackerrank.com/challenges/most-commons

s = input()
l = list(set(s))
d = {}
for i in l:
    count = s.count(i)
    d[i] = count
new_l = [(i, d[i]) for i in d]
new_l.sort(key=lambda x: (x[1]*-1, x[0]))
for i in new_l[:3]:
    print(*i)
