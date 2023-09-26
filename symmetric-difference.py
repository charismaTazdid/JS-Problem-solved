# Problem : https://www.hackerrank.com/challenges/symmetric-difference/

def solve(n, a, m, b):
    c = set()
    c = a.intersection(b)
    lista = list(a.difference(c))
    listb = list(b.difference(c))
    res = sorted(lista+listb)
    for i in res:
        print(i)


if __name__ == "__main__":
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    solve(n, a, m, b)
