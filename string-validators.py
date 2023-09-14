# Problem : https://www.hackerrank.com/challenges/string-validators

def check(s, isfun):
    return any(isfun(l) for l in s)


if __name__ == '__main__':
    s = input()
    print(check(s, str.isalnum))
    print(check(s, str.isalpha))
    print(check(s, str.isdigit))
    print(check(s, str.islower))
    print(check(s, str.isupper))
