# Problem: https://www.hackerrank.com/challenges/validating-uid

from re import match
T = int(input())


def check(s):
    if len(s) == len(set(s)) == 10:
        if match(r".*[0-9].*[0-9].*[0-9].*", s) is not None:
            if match(r"^[a-zA-Z0-9]+$", s) is not None:
                if match(r".*[A-Z].*[A-Z].*", s) is not None:
                    return "Valid"
    return "Invalid"


for _ in range(T):
    print(check(input()))
