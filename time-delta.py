# Problem: https://www.hackerrank.com/challenges/python-time-delta

from datetime import datetime

def time_delta(t1, t2):
    a = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    b = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    return str(int(abs((a-b).total_seconds())))
