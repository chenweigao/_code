class MyClass(object):

    message = "hello, weigao!"

    def show(self):
        print(self.message)
        print("Here is %s in %s" % (self.name, self.color))

    def __init__(self, name='unset', color='red'):
        print("Constructor is called")
        self.name = name
        self.color = color

    @staticmethod
    def printMessage():
        print("printMessage is called!")
        print(MyClass.message)

    @classmethod
    def createObject(cls, name, color):
        print("%s: %s, %s" % (cls.__name__, name, color))
        return cls(name, color)

class SubA(MyClass):
    def __init__(self):
        print("SubA is called!")
def test():
    # print(MyClass.message)
    # MyClass.message = "weigao, glod to see you again!"
    # print(MyClass.message)
    # inst = MyClass()
    # inst.message = "weigao, bye!"
    # inst.show()
    # print(MyClass.message)
    # inst2 = MyClass('chen')
    # inst2.show()
    MyClass.printMessage()
    inst3 = MyClass.createObject('chen', 'blue')
    print(inst3.message)


if __name__ == '__main__':
    test()
