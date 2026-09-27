class Employee:
    company = " Mercedes"

    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.secondname=lastname

    def getmailid(self):
        return(f"Mail id is {self.firstname}{self.secondname}@{Employee.company}.com")
    
    @classmethod
    def updatemail(cls,new_company):
        cls.company=new_company

Employee.updatemail("BMW")
emp=Employee("sachin","ramesh")
print(emp.getmailid())
print("hi")