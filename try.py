class computer:
    brand ="Sachin"

    def __init__(self,m1,m2):
        self. m1=m1 
        self.m2=m2 

    def reboot(self):
        print ("rebooting")
        return self.m1 + self.m2
    @classmethod
    def cls_comp(cls):
        # print(f"pritning class method {computer.brand}")
        return computer.brand
    @staticmethod
    def stat_method(a,b):
        
        return a*b
    print(len("brand"))
            
    

# print(computer.brand)

ob1=computer(2,3)
# print(ob1.reboot())

# print(computer.cls_comp())
# print(computer.stat_method(5,6))
# print(ob1.cls_comp())
print(ob1.stat_method(3,4))


    