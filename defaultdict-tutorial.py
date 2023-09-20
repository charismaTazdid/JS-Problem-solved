# Problem : https://www.hackerrank.com/challenges/defaultdict-tutorial


from collections import *
A, B = map(int, input().split())
dictA = defaultdict(list)
pos = 1
for i in range(A):
    letter = input()
    dictA[letter].append(pos)
    pos += 1

for i in range(B):
    letterB = input()
    if letterB in dictA:
        positions = dictA.get(letterB)
        print(" ".join(map(str, positions)))
    else:
        print(-1)
