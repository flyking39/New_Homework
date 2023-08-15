from abc import ABC, abstractmethod


class ElectronicProduct(ABC):
    """The initial abstract class"""
    @abstractmethod
    def __str__(self):
        pass


class Laptop(ElectronicProduct):
    """the class of Laptop that contains details and characteristics of the device """
    def __init__(self, *, screen_size, keyboard_size, prod_number, battery_capacity):
        self.name = 'Laptop'
        self.prod_number = prod_number
        self.screen_size = screen_size
        self.keyboard_size = keyboard_size
        self.battery_capacity = battery_capacity
        self.price = 50000

    def __str__(self):
        return f'{self.name} prod_number is {self.prod_number},  keyboard_board is {self.keyboard_size}, ' \
               f'and screen size is {self.screen_size}'


class Tablet(ElectronicProduct):
    """the class of Tablet that contains details and characteristics of the device"""
    def __init__(self, *, screen_size: int, processor_productivity: int, prod_number: int) -> None:
        self.name = 'Tablet'
        self.prod_number = prod_number
        self.screen_size = screen_size
        self.processor_productivity = processor_productivity
        self.price = 30000

    def __str__(self):
        return f'{str(self.name)} prod_number is {self.prod_number} , {self.screen_size} screen and ' \
               f'{self.processor_productivity} productivity'


class Customer:
    def __init__(self, *, budget: int, password: int):
        self.budget = budget
        self.password = password

    def get_password(self):
        return self.password

    def purchase(self, price: int):
        try:
            self.budget -= price
            print(self.budget)
        except Exception as x:
            print(x, 'not enough money to implement your request')


A = Laptop(screen_size=14, keyboard_size=12, prod_number=457457, battery_capacity=15000)
B = Tablet(prod_number=768768, screen_size=12, processor_productivity=5000)
list_of_goods = [A, B]
C = Customer(budget=int(input('Enter your budget')), password=int(input('Enter password')))


def user_search():
    user_input = str(input('Enter a name of the good you are looking for: ')).upper()
    try:
        for good in list_of_goods:
            if user_input != good.name:
                continue
            else:
                item_purchase(good)
    except RuntimeError:
        print(f'{user_input} has not been found, try again')


def item_purchase(good) -> None:
    print(good)
    user_decision = str(input('Enter continue if you want '
                              'to make a purchase or enter cancel if you do not: '))
    if user_decision == 'continue':
        user_password = int(input('Enter password '))
        if user_password == C.get_password():
            C.purchase(good.price)
            print(f'{good.name} has been purchased, show {good.prod_number} '
                  f'to get your purchase in the chosen delivery store')
            list_of_goods.remove(good)
        else:
            print(f'{user_password} is not valid, try again with the proper password')
    else:
        user_search()


user_search()
