# Problem: https://www.hackerrank.com/challenges/any-or-all

i, numbers, y, z = input(), list(map(int, input().split())), True, False
p, l = [z for x in numbers if x < 0], [y if x > 0 and str.join(
    '', str(x)) == str.join('', reversed(str(x))) else z for x in numbers]
[print(z) if p else print(any(l))]
