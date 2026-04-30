'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.leg_count = 4
    def info(self):
        print(f'Имя собаки: {self.name}')
        print(f'Возраст собаки: {self.age}')
animal1 = Dog('Bobik', 10)
animal2 = Dog('Sharik', 4)
animal1.info()
animal2.info()
print(animal1.leg_count)
animal2.leg_count += 1
print(animal2.leg_count)
'''

'''
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimeter(self):
        return self.a*2 + self.b*2
rect1 = Rectangle(5, 10)
print(rect1.area())
print(rect1.perimeter())
'''


'''
Реализовать класс Product, у объектов класса будет имя и цена
Реализовать метод get_info() информация о товаре
Реализовать метод change_price(amount) - изменить цену на amount
'''
from typing import Any


class Product:
    def __init__(self, name: str=None, price:int=0):
        self.name = name
        try:
            self.price = int(price)
        except:
            print(f'Ошибка при объявлении цену у {name}')
    def get_info(self):
        print(f'Название товара: {self.name}; цена - {self.price}')
    def change_price(self, amount):
        try:
            self.price += int(amount)
        except:
            print(f'У {self.name} ошибка при измении цены, проверьте значение')

class Food(Product):
    def __init__(self, name: str = None, price: int = 0, exp_date: str=None):
        super().__init__(name, price)
        self.exp_date = exp_date
    def get_info(self):
        print(f'Название товара: {self.name}; цена - {self.price}; срок годности - {self.exp_date}')

class Clothes(Product):
    def __init__(self, name: str = None, price: int = 0, size: int=0):
        super().__init__(name, price)
        self.size = size
    def get_info(self):
        print(f'Название товара: {self.name}; цена - {self.price}; размер - {self.size}')    
class Drinks(Food):
    def __init__(self, name: str = None, price: int = 0, exp_date: str = None, volume:float=0.0):
        self.volume = volume
        super().__init__(name, price, exp_date)
    def get_info(self):
        print(f'Название товара: {self.name}; цена - {self.price}; срок годности - {self.exp_date}; объем - {self.volume}')

class Cart:
    def __init__(self):
        self.List_products = []
    def add_item(self, item):
        self.List_products.append(item)
    def show_items(self):
        print('======Товары======')
        for item in self.List_products:
            item.get_info()
    def total_price(self):
        if not self.List_products:
            return 'Корзина пуста'
        total = 0
        for item in self.List_products:
            total += item.price
        return total

prod1 = Product('PC', 20000)
moloko = Food('Moloko', 120, '04.04.2026')
moloko.get_info()
moloko.change_price(-20)
moloko.get_info()
cola = Drinks('Cola', 120, '0000', 0.5)
cola.change_price(20)
cola.get_info()
cart1 = Cart()
cart1.add_item(moloko)
cart1.add_item(cola)
cart1.add_item(prod1)
cart1.show_items()
print(cart1.total_price())