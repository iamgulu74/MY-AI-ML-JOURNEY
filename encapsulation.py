class bankaccount:
    def __init__(self, owner, balance,pin):
        self.owner = owner #public attribute
        self.__balance = balance #private attribute
        self._pin = pin #protected attribute
        
    def get_balance(self):#getter method for private attribute
        return self.__balance
    
    def set_pin(self, new_pin):#setter method for protected attribute
        self._pin = new_pin

account1 = bankaccount("Alice", 1000, 1234)
print(f"Account Owner: {account1.owner}")
account1.set_pin(5678)
print(f"New PIN set successfully.")
print(f"Account Balance: {account1.get_balance()}")
print(account1._pin) 
