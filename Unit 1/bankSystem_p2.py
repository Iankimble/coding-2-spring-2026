class IanFirstBank:
    def __init__(self, name, password, address, balance):
        self.name = name
        self.password = password
        self.address = address
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('Thanks '+ self.name +' your new balance is ' + str(self.balance))
    
    def withdraw(self, amount):
        self.balance -= amount
        print('Thanks '+ self.name +' your new balance is ' + str(self.balance))

    # def accessAccount(self):
    #     return
    
    # def closeAccount(self):
    #     return

account_1 = IanFirstBank('John', '123ABC','NA', 100)
account_2 = IanFirstBank('Ashley', '321ABC','NA', 200)

account_1.deposit(50)
account_2.withdraw(60)

users = []

def createAccount():
    print('Welcome to Ians first bank.')
    print("Please complete the  following questions to create your account: ")
    name= input("name: ")     
    password= input("password: ")
    address= input("address: ")
    balance= input("How much would you like to add to the new account?: ")   
    
    print("Congratulations! your bank account is done.")

    account_3= IanFirstBank(name, password, address, balance)
    users.append(account_3)

createAccount()

print(users)

# def runApp():
#     print('welcome to the bank. Please enter your pin')