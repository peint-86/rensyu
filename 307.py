a,b=input().split()
oya={1:int(a),2:int(b)}
n=int(input())
for i in range(n):
    c,d=input().split()
    c=int(c)
    d=int(d)
    if oya[1]>c:
        print("High")
    elif oya[1]==c:
        if oya[2]<d:
            print("High")
        else:
            print("Low")
    elif oya[1]<c:
        print("Low")

      
#C017
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