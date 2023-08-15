class BankAccount:
    def __init__(self, *, account_number: int, account_holder: str, balance: int):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount: int):
        """
        adds money on the account
        :param amount: the summ the holder is allocating to his or her account
        :return: the result of operation initial summ + amount
        """
        self.__balance += amount
        print(f'confirmation, added on {amount}')
        print(f'{self.__balance} is your balance')
        return f'{self.__balance}'

    def withdraw(self, amount: int):
        """
        withdraws money from the account
        :param amount: the summ the holder is withdrawing to his or her account
        :return:
        """
        if self.__balance >= amount > 0:
            self.__balance -= amount
            print(f'confirmation, withdrawn {amount}')
            print(f'{self.__balance} is your balance')
            return f'{self.__balance}'
        else:
            print(f'An unacceptable number, {amount}')

    def get_account_name(self):
        return self.__account_holder

    def get_account_number(self):
        """
        returns account_number that it can be used as key in the dictionary
        :return:
        """
        return self.__account_number

    def reallocation(self, other, summ: int):
        try:
            self.__balance -= summ
            other.__balance += summ
            print(f'your balance is {self.__balance}, the balance of your receiver is {other.__balance}')
            with open('notifications.txt', 'a') as quick_file:
                quick_file.write(f'{other.__account_number}: {self.__account_holder} has dispatched you {summ} '
                                 f'and your current balance is {other.__balance}' + '\n')
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


def notifications_check(parameter: int):
    try:
        with open('notifications.txt', 'r') as quick_file:
            note = quick_file.readlines()
            try:
                for line in note:
                    print(line)
                    print(line.split(':')[0])
                    print(str(parameter), 'parameter')
                    if line.split(':')[0] == str(parameter):
                        print(line)
                    else:
                        print('no message')
                        continue
            except RuntimeError:
                print('you have no notifications')
    except Exception as x:
        print(x)


def prod_number_identification():
    """
    verification of user prod_number_identity via account number input,
    if prod_number is valid it activates function financial_operations otherwise raises error
    :return:
    """
    account_number = int(input('Enter account number: '))
    if account_number in dictionary_of_holders.keys():
        notifications_check(dictionary_of_holders.get(account_number))
        financial_operations(account_number)
    else:
        raise Exception('You have entered the wrong account number, check and try again or consult support service')


def financial_operations(account_number: int):
    """
    implements one of available class functions
    :param account_number: is imported from prod_number identification function and is a key of dictionary
    that  the value as a class with particular inf
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


prod_number_identification()
# inquire the matter with additional condition in function while entrance
#  possible ways to simplify the code
# except with personal exception
# make files with recent notifications regarding any implemented transactions
# add exception for self input
# follow up what file tell means!!