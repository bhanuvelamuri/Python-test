print('hello')
print("========if=else===============")
greetings = "welcome"
if greetings != "welcome":
    print("good morning")
else:
    print("bye")
add = 5
mul = 5.3
div = 2
percentile = 2.1
sub = 1
for i in range(1, 7):
    print(add + i)
print("*********")
for j in range(1, 7):
    print(sub + j)
print("*********")
for k in range(1, 7):
    print(mul + k)
print("*********")
for l in range(7):
    print(div + l)
print("*********")
for m in range(1, 7):
    print(percentile + m)
print("=======While loop=================")
it = 8
while it > 1:
    if it == 4:
        print("matches")
    else:
        print("not matches")
    print(it)
    it = it - 1
    continue
print("======== Functions ================")


def Greetings(name):
    print("Good Morning " + name)


def Add(a, b):
    return a + b


Greetings("bhanu pratap")
print("======== add ================")
print(Add(5, 6))
print("======== OOPS ================")
print("======== Classes ================")


class Calculator:
    num = 100

    def __init__(self, a, b):
        self.first = a
        self.second = b
        print("default execution when obj is created")

    def getData(self):
        print("print data")

    def Add(self):
        print(self.first)
        print(self.second)
        return self.first + self.second + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.num)
print(obj.Add())
print("======================")
obj1 = Calculator(4, 3)
obj1.getData()
print(obj1.num)
print(obj1.Add())

print("======== Inheretance ================")


