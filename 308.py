

def is_same_type(wreath1, wreath2):
    # リースを回転させて、同じ種類かどうかを判定する
    for i in range(len(wreath1)):
        if wreath1 == wreath2:
            return "Yes"
        # リースを1つ分回転させる
        wreath1 = wreath1[1:] + wreath1[0]
    return "No"

n = int(input())
wreath1 = input()
wreath2 = input()

print(is_same_type(wreath1, wreath2))

n=int(input())
f_1=(input())
f_2=(input())
for i in range(n):
    if f_1 == f_2:
            print("Yes")
            break
        # リースを1つ分回転させる
    elif i==n-1:
        print("No")
    else:
        f_2= f_2[1:] + f_2[0]
    
    
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

for i in range(n):
    for j in range(i+1, n):#この二行大事、前後の比較を可能にしている
        if roster[i].old > roster[j].old:
            roster[i], roster[j] = roster[j], roster[i]

for student in roster:
    print(student.name, student.old, student.birth, student.state)

#final problem url https://paiza.jp/works/mondai/class_primer/class_primer__change
class Student:#tenpure
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

    def change_name(self, name):
        self.name = name


n, k = [int(x) for x in input().split()]

roster = [None] * n#tenpure
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

for i in range(k):
    index, new_name = input().split()
    roster[int(index) - 1].change_name(new_name)

for student in roster:#tepure
    print(student.name, student.old, student.birth, student.state)

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