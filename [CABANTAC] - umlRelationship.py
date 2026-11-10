from abc import ABC, abstractmethod

# 1. INHERITANCE
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# 2. REALIZATION
class Payable(ABC):
    @abstractmethod
    def pay(self):
        pass


class Payment(Payable):
    def pay(self):
        print("Payment successful")


# 3. COMPOSITION
class Room:
    def display(self):
        print("This is a room")


class House:
    def __init__(self):
        self.room = Room()

    def show_house(self):
        self.room.display()
        print("This is a house")


# 4. AGGREGATION
class Book:
    def display(self):
        print("This is a book")


class Library:
    def __init__(self, book):
        self.book = book

    def show_library(self):
        self.book.display()
        print("This is a library")


# 5. ASSOCIATION
class Order:
    def display(self):
        print("This is an order")


class Customer:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def show_orders(self):
        for order in self.orders:
            order.display()


# 6. DEPENDENCY
class Document:
    def display(self):
        print("Printing document")


class Printer:
    def print_document(self, doc):
        doc.display()


# MAIN PROGRAM
if __name__ == "__main__":

    print("\n1. INHERITANCE")
    dog = Dog()
    dog.eat()
    dog.bark()

    print("\n2. REALIZATION")
    payment = Payment()
    payment.pay()

    print("\n3. COMPOSITION")
    house = House()
    house.show_house()

    print("\n4. AGGREGATION")
    book = Book()
    library = Library(book)
    library.show_library()

    print("\n5. ASSOCIATION")
    customer = Customer()
    order = Order()
    customer.add_order(order)
    customer.show_orders()

    print("\n6. DEPENDENCY")
    printer = Printer()
    document = Document()
    printer.print_document(document)