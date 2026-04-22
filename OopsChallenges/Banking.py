class Account:
    def __init__(self,id,holder_name,balance):
        self.id = id
        self.holder_name = holder_name
        self._balance = balance

    def check_balance(self):
        print("Account balance: ",self._balance)

    def deposite(self,amount):
        if amount  > 0:
            self._balance += amount
            print("Account balcne after deposition of Rs. : ",self._balance)
        else:
            print("Deposition amount should be greater than 0")

    def withdraw(self,amount):
        if self._balance >= amount and amount > 0 :

            self._balance -= amount
            print("Accouunt balance after withdrawl: ",self._balance)
        else:
            print("Insufficient balancce")

class SavingAccount(Account):  #inheritance

    def caculate_interest(self):
        if self._balance != 0:
            INTERESTE_RATE = 0.04 # 4% interest rate
            interest = self._balance * INTERESTE_RATE
            print(" Toatal interaste: "+interest)
class CurrentAccount(Account):

    def withdraw(self, amount):   #polymorphism  : override
        OVERDRAFT = 1000

        if self._balance + OVERDRAFT >= amount:

            self._balance -=  amount
            print(f"Account balance after withdraw: {self._balance}")

class Bank:

    def __init__(self,id, city):
        self.id = id
        self.city = city 
        self.__account = {}
    def createAccount(self,id,holder_name,type):
        if type == "savings":
            new_account = SavingAccount(id,holder_name,1000)
            print("Savings Accouunt created successful!!!!")
        elif type == "current":
            new_account = CurrentAccount(id,holder_name,100)
            print(" Current Accouunt created successful!!!!")
        return new_account
    def get_account(self,id):
        if id not in self.__account:
            print("Account not found!!")
        else:
            account = self.__account[id]
            print(f" Account id : {self.id} \n Account holder name : {self.holder_name}")
            return account
     
nbk = Bank("Nanjunda Bank Of Karnataka ","Nagamangala")

s1 = nbk.createAccount(10001,"Nanjunda","savings")

s1.check_balance()
s1.deposite(5670)
s1.withdraw(6000)
s1.check_balance()

c1 = nbk.createAccount(10002,"Charan","current")

c1.check_balance()
c1.withdraw(200)

nbk.get_account(10002)