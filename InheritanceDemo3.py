# Multiple Inheritance

class ClassA():
    def methodA(self):
        print("I am in class A")

    def hello_world(self):
        print("Hello from Class A")

class ClassB():
    def methodB(self):
        print("I am in class B")

    def hello_world(self):
        print("Hello from Class B")

#Inheriting multiple class in ClassC
class ClassC(ClassA, ClassB): # here this is MRO which Method Resolution Order
    def methodC(self):
        print("I am in class C")

    def hello_world(self):
        print("Hello from Class C")

obj1=ClassC()
obj1.methodA()
obj1.methodB()
obj1.methodC()
obj1.hello_world()
print(ClassC.mro())