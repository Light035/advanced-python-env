class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough balance")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount("Light", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())
