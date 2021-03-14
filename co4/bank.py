class bank():
    def __init__(self):
        self.balance=0
        print("YOUR ACCOUNT IS NOW CREATED")
    def deposit(self):
        amount=float(input("\n enter the amount to be deposited : "))
        self.balance+=amount
        print("\n your amount is deposited : ",amount)
    def withdraw(self):
        amount=float(input("\n enter the amount to be withdrawn : "))
        if self.balance >= amount:
            self.balance-=amount
            print("you have withdrew : ",amount)
        else:
            print("insufficient balance ")
a=bank()
a.deposit()
a.withdraw()