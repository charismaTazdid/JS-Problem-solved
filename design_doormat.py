# Problem : https://www.hackerrank.com/challenges/designer-door-mat/

def design_doormat(n, m):

    pat = '.|.'

    for i in range(1, n, 2):
        print((pat*i).center(m, '-'))

    print("WELCOME".center(m, '-'))

    for i in reversed(range(1, n, 2)):
        print((pat*i).center(m, '-'))


if __name__ == "__main__":
    n, m = map(int, input().split())
    design_doormat(n, m)
