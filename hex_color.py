# Problem : https://www.hackerrank.com/challenges/hex-color-code/
import re

pattern = re.compile(r"(#[\da-f]{3}|#[\da-f]{6})(?=[;,)])", re.IGNORECASE)

N = int(input())

ls = [input() for _ in range(N)]
S = "\n".join(ls)

if pattern.search(S):
    for match in re.findall(pattern, S):
        print(match)
