#Single level inheritance
class Base:
    name="Anshul"
    def baseMethod(self):
         print("I am in base class")

class Child(Base):  #here inheriting Base class in child class
    language = "Python"
    def childMethod(self):
        print("I am in child class")

c=Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.language)
