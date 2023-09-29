# Problem : https://hackerrank.com/challenges/itertools-combinations

from itertools import combinations
string, size = input().split()
combination_list = []
for i in range(int(size)):
    combination_list += list(combinations(sorted(string), i + 1))
print("\n".join(list(map(''.join, combination_list))))
