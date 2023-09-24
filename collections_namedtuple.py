# Problem : https://www.hackerrank.com/challenges/py-collections-namedtuple

from collections import namedtuple

num_student = int(input())
Student = namedtuple("Student", ([x for x in input().split()]))
students = []

for line in range(num_student):
    line = input().split()
    student = Student._make(line)
    students.append(student)

total = 0
for item in students:
    i = 0
    mark = list(map(int, item.MARKS.split()))
    total += mark[i]
    i += 1

print(total/num_student)
