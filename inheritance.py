class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def get_salary(self):
        print(f"salary of parent {self.name} is {self.salary}")
        print("hiiii")

    def set_salary(self,salaryy):
        self.salary=salaryy

    def __str__(self):
        return(f"printing the object from parent class employee")


class Person:
    def __init__(self,sex):
        self.sex=sex

    def set_sex(self):
        print(f"sex of the person is {self.sex}")

class Developer(Employee,Person):
    def __init__(self, name, age, salary,sex,language):
        self.language=language
        Employee.__init__(self,name, age, salary)
        Person.__init__(self,sex)

    
    def get_salary(self):
        print(f"salary of child {self.name} is {self.salary}") 

    def all_in(self):
        print(f"name is {self.name}, \nage is {self.age}, \nsalary is {self.salary}, \nsex is {self.sex}, \nlanguage is {self.language}")
            

dev=Developer("sachin",24,110000,"male","python")
# print(dev.salary)
# dev.set_salary(22000)
# dev.get_salary()
# print(dev)
# dev.set_sex()
dev.all_in()