class BankAccount:
    def __init__(self, *, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self, amount):
        pass

    def __str__(self):
        pass
