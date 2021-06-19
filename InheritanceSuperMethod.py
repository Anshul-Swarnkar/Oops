class BaseClass:
    def hello_world(self):
        print("Hello Python from Base")

    def Bye(self):
        print("Bye Bye")

class ChildClass(BaseClass):
    def hello_world(self):
        #BaseClass.hello_world(self) #here we are calling same method of BaseClass
        super().hello_world()   # here you can use Super method instead of above line of code
        super().Bye()
        print("Hello Python from Child")

obj1=ChildClass()
obj1.hello_world()

