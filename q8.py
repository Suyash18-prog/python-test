# implement a BankAccount class with deposit(), withdraw(), and balance() methods.

class BankAccount :

    def __init__(self,account_number,balance):
        self.acount_number = account_number
        self.balance = balance

    def deposit (self,amount):
        balance+=amount
        print(f"{amount} has been credited to your account and your balnce is{self.balance}")
    
    def withdraw(self,amount):
        balance-=amount
        print(f"{amount} has been debited from your account and your balnce is{self.balance}")
    
    def check_balnce(self):
        print(f"Your balance is {self.balance} !")

account1 = BankAccount(12345125,5000)