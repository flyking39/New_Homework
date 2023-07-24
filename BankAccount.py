import random


class BankAccount:
    def __init__(self, *, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # def set_balance(self, new_balance):
    #     self.__balance = new_balance
    #     return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(f'confirmation, added on {amount}')

    def withdraw(self, amount: int):
        if self.__balance >= amount > 0:
            self.__balance -= amount
            print(f'confirmation, withdrawn {amount}')
        else:
            print(f'An unacceptable number, {amount}')

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f'your balance equals {self.__balance}'


list_of_names = ['Jessy', 'Martin', 'Lissy']
list_of_surnames = ['Carter', 'Lee', 'Mccarthy']
list_of_account_holders = []

for _ in range(3):
    user_number = random.randint(9999, 100000)
    user_name = random.choice(list_of_surnames) + random.choice(list_of_names)
    user_balance = random.randint(9999, 100000)
    list_of_account_holders.append(BankAccount(account_number=user_number, account_holder=user_name, balance=user_balance))

print(list_of_account_holders)

for holder in list_of_account_holders:
    holder.deposit(random.randint(9999, 100000))
    holder.get_balance()
    holder.withdraw(random.randint(9999, 100000))
    print(holder)

# create a function with money allocation from one account to another



