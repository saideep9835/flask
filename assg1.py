class Bank_Account:
    def __init__(self):
        self.owner = "Saideep"
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self):
            amount=6799.88
            self.balance += amount
            print(" Amount Deposited: ",amount)
  
    def withdraw(self):
        amount = 8976.00
        if (self.balance>=amount):
            self.balance-=amount
            print(" You Withdrew: ", amount)
        else:
            print(" Insufficient balance in your Account to Withdraw")
            print(" Your Account balance is : ",self.balance)

  
    def display(self):
        print("Account owner : ", self.owner)
        print(" Net Available Balance = ",self.balance)
  

s = Bank_Account()
   
s.display()
s.deposit()
s.display()
s.withdraw()
s.display()

s.deposit()
s.display()
s.withdraw()
s.display()

s.deposit()
s.display()
s.withdraw()
s.display()
