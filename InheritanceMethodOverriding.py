class A:
    def sum(self):
        print("Calling from class A- sum of two number is 15")

class B(A):
    def sum(self):
        print("calling from class B- sum of two number is 25")

class C(B):
    def sum(self):
        print("Calling from C- Sum of two numbers is 50")

obj1=C()
obj1.sum()  