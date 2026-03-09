import random

class IanFirstBank:
    def __init__(self, name, age, balance, accountNumber, phone):
        self.name = name
        self.age = age
        self.balance = balance
        self.accountNumber = accountNumber
        self.phone = phone

    def deposit(self, amount):
        self.balance += amount
        print('you have '+ str(self.balance))
        
    def withdraw(self, amount):
        self.balance -= amount
        print('you have '+ str(self.balance))

    def checkBalance(self):
        print('you have '+ str(self.balance))

account_1 = IanFirstBank("Bob", 45, 300, '124ab34', 'NA')
account_2 = IanFirstBank("Stacy", 25, 100, '154av34', 'NA')

#account_1.checkBalance()
#account_1.deposit(500)
#account_1.withdraw(150)

#account_2.checkBalance()
#account_2.deposit(100)
#account_2.withdraw(50)

bankUsers = [account_1, account_2]

def createAccount():
    print("Welcome to Ians First Bank")
    print("Please complete the form to craeate an account.")

    name = input("please type in your name: ")
    age = int(input("please type in your age: "))
    balance = int(input("please type in how much you want to deposit: ")) 
    accountNumber = random.randrange(100,500)
    
    print("Congrats! Your acount is complete")
    
    account = IanFirstBank(name, age, balance,accountNumber,'na')   
    bankUsers.append(account)
    
print(bankUsers)

def mainBankApp():
    print("Welcome")
    print('Are you a existing custommer or new cutomer? ')
    print("Please type 1 for existing and 2 for new member: ")
    answer = input()
    if answer == 1:
        print('Welcome back')
        # find account/ deposiit/ withdraw
    elif answer == 2:
        createAccount()

mainBankApp()