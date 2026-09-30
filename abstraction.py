from abc import ABC, abstractmethod


class paymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass
class Paypal(paymentGateway):
    def pay(self):
        print("paying using paypal")
class Razorpay(paymentGateway):
    def py(self):
        print("payg using razorpay")

class Purchase:

    def __init__(self,gateway):
        self.gateway=gateway
        
    def checkout(self):
        print("cjecking out")

        self.gateway.pay()
gateway1=Razorpay()
gateway2=Paypal()
purchase=Purchase(gateway2)
purchase.checkout()
purchase=Purchase(gateway1)
purchase.checkout()