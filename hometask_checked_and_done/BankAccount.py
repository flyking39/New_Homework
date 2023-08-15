# import random
#
#
# class BankAccount:
#     def __init__(self, *, account_number, account_holder, balance):
#         self.__account_number = account_number
#         self.__account_holder = account_holder
#         self.__balance = balance
#
#     # def set_balance(self, new_balance):
#     #     self.__balance = new_balance
#     #     return self.__balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f' confirmation, added on {amount}')
#
#     def withdraw(self, amount: int):
#         if self.__balance >= amount > 0:
#             self.__balance -= amount
#             print(f' confirmation, withdrawn {amount}')
#         else:
#             print(f'An unacceptable number, {amount}')
#
#     def get_balance(self):
#         return self.__balance
#
#     def __str__(self):
#         return f' your balance equals {self.__balance}'
#
#     def reallocation(self):
#         pass
#
#
# list_of_names = ['Jessy', 'Martin', 'Lissy']
# list_of_surnames = ['Carter', 'Lee', 'Mccarthy']
# list_of_account_holders = []
#
# for _ in range(3):
#     user_number = random.randint(9999, 100000)
#     user_name = random.choice(list_of_surnames) + random.choice(list_of_names)
#     user_balance = random.randint(9999, 100000)
#     list_of_account_holders.append(BankAccount(account_number=user_number,
#                                                account_holder=user_name, balance=user_balance))
#
# print(list_of_account_holders)
#
# for holder in list_of_account_holders:
#     holder.deposit(random.randint(9999, 100000))
#     holder.get_balance()
#     holder.withdraw(random.randint(9999, 100000))
#     print(holder)
#
# # create a function with money reallocation from one account to another
#
#
# def financial_operations():
#     pass

class BankAccount:
    def __init__(self, *, account_number: int, account_holder: str, balance: int):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount: int):
        """
        adds money on the account
        :param amount:
        :return:
        """
#and > 0
        self.__balance += amount
        print(f'confirmation, added on {amount}')
        print(f'{self.__balance} is your balance')
        return f'{self.__balance}'

    def withdraw(self, amount: int):
        """
        withdraws money from the account
        :param amount:
        :return:
        """
        if self.__balance >= amount > 0:
            self.__balance -= amount
            print(f'confirmation, withdrawn {amount}')
            print(f'{self.__balance} is your balance')
            #self.__str__()
            return f'{self.__balance}'
        else:
            print(f'An unacceptable number, {amount}')

    def get_account_number(self):
        """
        returns account_number that it can be used as key in the dictionary
        :return:
        """
        return self.__account_number

    # def __str__(self):
    #     return f' your balance equals {self.__balance}'

    def reallocation(self, other, summ: int):
        """
        reallocates money from one account to another one
        :param other: value of the dictionary( class with inf of money receiver)
        :param summ: summ of money the dispatcher inputs and subsequently sends to the receiver account
        :return:
        """
        try:
            self.__balance -= summ
            other.__balance += summ
            print(f'your balance is {self.__balance}, the balance of your receiver is {other.__balance}')
        except Exception as x:
            print(x)


A = BankAccount(account_number=346346, account_holder='Billy', balance=46000)
B = BankAccount(account_number=678967, account_holder='Martin', balance=50000)
C = BankAccount(account_number=768324, account_holder='Henry', balance=20000)
D = BankAccount(account_number=452473, account_holder='Jessy', balance=67000)
E = BankAccount(account_number=196397, account_holder='Candra', balance=58000)

dictionary_of_holders = {A.get_account_number(): A, B.get_account_number(): B,
                         C.get_account_number(): C, D.get_account_number(): D,
                         E.get_account_number(): E}


def identification():
    """
    verification of user identity via account number input,
    if valid it activates function financial_operations otherwise raises error
    :return:
    """
    account_number = int(input('Enter account number: '))
    if account_number in dictionary_of_holders.keys():
        financial_operations(account_number)
    else:
        raise Exception('You have entered the wrong account number, check and try again or consult support service')


def financial_operations(account_number: int):
    """
    implements one of available class functions
    :param account_number: is imported from identification function and is a key of dictionary
    that provides the value as a class with particular inf
    :return:
    """
    holder_command = str(input('Enter the operation you are to implement: '))
    if holder_command.lower() == 'deposit':
        dictionary_of_holders.get(account_number).deposit(int(input('Enter the summ of money you are to allocate: ')))
    elif holder_command.lower() == 'withdraw':
        dictionary_of_holders.get(account_number).withdraw(int(input('Enter the summ of money you are to allocate: ')))
    elif holder_command.lower() == 'reallocation':
        dictionary_of_holders.get(account_number).reallocation(dictionary_of_holders.get(int(input(
            'Enter the number of holder you are dispatching money to: '))), int(input('Enter the summ of money: ')))
    else:
        print('you entered wrong command, try again')


identification()

# inquire the matter with additional condition in function while entrance
#  possible ways to simplify the code
# except with personal exception
# make files with recent notifications regarding any implemented transactions
