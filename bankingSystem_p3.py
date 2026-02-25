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

account_1.checkBalance()
account_1.deposit(500)
account_1.withdraw(150)

account_2.checkBalance()
account_2.deposit(100)
account_2.withdraw(50)
