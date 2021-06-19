# Multilevel Inheritance

class classA():
    def methodA(self):
        print("I am in class A")


class classB(classA):
    def methodB(self):
        print("I am in class B")

class classC(classB):
    def methodC(self):
        print("I am in class C")

obj1=classC()
obj1.methodA()
obj1.methodB()
obj1.methodC()
