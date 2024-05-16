class BankAccount:
    def __init__(self, name:str, acc_num:str, balance:float):
        self.__name = name
        self.__account_number = acc_num
        self.__balance = balance
    
    def deposit(self, amount:float):
        if(amount > 0):
            self.__balance += amount
            self.__service_charge()
    
    def withdraw(self, amount:float):
        if (amount > 0 and (self.__balance-amount) >= self.__balance*0.01):
            self.__balance -= amount
            self.__service_charge()
    
    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        if(self.__balance - self.__balance*0.01 >= 0):
            self.__balance -= self.__balance*0.01

if __name__ == "main":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
