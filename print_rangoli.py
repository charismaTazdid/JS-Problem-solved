# Problem: https://www.hackerrank.com/challenges/alphabet-rangoli

def print_rangoli(size):
    c = [chr(i) for i in range(97, 97+size)]
    d = list(reversed(c))
    for i in range(size):
        b = d[:i+1] + c[size-i:]
        h = '-'.join(b)
        print(h.center(4*size-3, '-'))
    for i in range(size-2, -1, -1):
        b = d[:i+1] + c[size-i:]
        h = '-'.join(b)
        print(h.center(4*size-3, '-'))
    return c


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
