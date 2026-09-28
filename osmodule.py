class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self.__age = age

    def showage(self):
        print(f"agie is {self.__age}")
emp = Employee("Sac",24)
emp.showage() 
print(emp.__age)

        