# Problem: https://www.hackerrank.com/challenges/py-set-mutations

a = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    b = input().split()
    for j in range(N):
        B = set(map(int, input().split(' ', int(b[1]))))
        if b[0] == 'update':
            A.update(B)
        elif b[0] == 'intersection_update':
            A.intersection_update(B)
        elif b[0] == 'difference_update':
            A.difference_update(B)
        elif b[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(B)
        break
print(sum(A))
