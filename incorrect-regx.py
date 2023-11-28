
import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)


#problem link: https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true