class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name

    def change_num(self, newnum):
        self.number = newnum

    def change_name(self, newname):
        self.name = newname

employees = []
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "make":
        employees.append(Employee(int(command[1]), command[2]))
    elif command[0] == "getnum":
        print(employees[int(command[1])-1].getnum())
    elif command[0] == "getname":
        print(employees[int(command[1])-1].getname())
    elif command[0] == "change_num":
        employees[int(command[1])-1].change_num(int(command[2]))
    elif command[0] == "change_name":
        employees[int(command[1])-1].change_name(command[2])


class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name

    def change_num(self, number):
        self.number = number

    def change_name(self, name):
        self.name = name

#模範解答

n = int(input())

roster = []
for _ in range(n):
    values = input().split()

    query = values[0]
    if query == "make":
        number = int(values[1])
        name = values[2]
        roster.append(Employee(number, name))
    else:
        index = int(values[1]) - 1
        if query == "getnum":
            number = roster[index].getnum()
            print(number)
        elif query == "getname":
            name = roster[index].getname()
            print(name)
        elif query == "change_num":
            new_num = int(values[2])
            roster[index].change_num(new_num)
        else:
            new_name = values[2]
            roster[index].change_name(new_name)

            n, m = map(int, input().split())
            sushi_order = list(map(int, input().split()))
            can_pack = True
            for _ in range(m-1):
                next_sushi_order = list(map(int, input().split()))
                for i in range(n):
                    if sushi_order[i] != next_sushi_order[i]:
                        can_pack = False
                        break
                if not can_pack:
                    break
                sushi_order = next_sushi_order

            if can_pack:
                print("Yes")
            else:
                print("No")
#c129
n,m=map(int,input().split())
tehon=[]
test=[]
for _ in range(m):
    a=int(input())
    tehon.append(a)
for _ in range(m):
    a=int(input())
    test.append(a)

if max(tehon)==max(test):
    print("Yes")
else:
    print("No")