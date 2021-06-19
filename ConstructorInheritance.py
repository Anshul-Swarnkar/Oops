class A:
    def __init__(self):
        print("I am in class A")

class B(A):
    def __init__(self):
        #A.__init__(self)
        super().__init__()
        print("I am in class B")

class C(B):
    def __init__(self):
        super().__init__()
        print("I am in class C")

obj1=C()

# __init__(self) is a constructor here