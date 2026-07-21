class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ₹", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn ₹", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("\n----- Account Details -----")
        print("Account Holder :", self.name)
        print("Current Balance: ₹", self.balance)


account = BankAccount("Tanvi", 5000)

account.display()
account.deposit(2000)
account.withdraw(1000)
account.display()

#output
#----- Account Details -----
#Account Holder : Tanvi
#Current Balance: ₹ 5000
#Deposited ₹ 2000
#Withdrawn ₹ 1000

#----- Account Details -----
#Account Holder : Tanvi
#Current Balance: ₹ 6000
