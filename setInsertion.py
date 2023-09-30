# Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
set1 = A & B
print(len(set1))
