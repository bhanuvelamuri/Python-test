from demo import Calculator


class child(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self, 2, 4)

    def getCompletedata(self):
        return self.num2 + self.first + self.second + Calculator.num


obj2 = child()
print(obj2.getCompletedata())
