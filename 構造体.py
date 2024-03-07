class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

mike = person('hulo', 18)

print(f'name: {mike.name}, age: {mike.age}')

#name: hulo, age: 18

class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state


n = int(input())

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

k = input()
for student in roster:
    if student.old == k:
        print(student.name)
        break