from abc import ABC, abstractmethod
import os


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass



class Book:
    def __init__(self, isbn ,title,author, price):
        self.__isbn = isbn
        self.__title = title
        self.__author =author
        self.__price = price

    def __str__(self):
        return 'Book' + self.__isbn + ' , ' + self.__title + ',' + self.__author  + self.__price
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @isbn.setter
    def author(self, author):
        self.__author = author
    @property
    def price(self):
        return self.__price

    @isbn.setter
    def price(self, price):
        self.__isbn = price
    
    def display(self):
        pass

class OrderItem:
    def __init__(self, isbn, quantity):
        self.__isbn = isbn
        self.__quantity = quantity
        
    def __str__(self):
        return 'OrderItem ' + self.__isbn + ',' + self.__quantity
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn


class Order:
    def __init__(self):
        self.__items  = []
    
    def addOrder(self, isbn, quantity):
        self.__items.append(OrderItem(isbn, quantity))
    

class BookList:
    def __init__(self):
        self.__books = []

    def addBook(self,book):
        self.__books.append(book)
    
    def display(self):
        for book in self.__books:
            book.display()

class Invoice:
    def __init__(self) -> None:
        pass

class DisplayBookListCommand(Command):
    def __init__(self, bookList):
        self.__bookList = bookList

    def execute(self):
        self.__bookList.display()

class SubmitOrderCommand(Command):
    def __init__(self, order):
        self.__order = order

    def execute(self):
        isbn = input()
        quantity = input()
        self.__order.submitOrder(isbn,quantity)

class DisplayInvoiceCommand(Command):
    def __init__(self,invoice):
        self.__invoice = invoice

    def execute(self):
        self.__invoice.display()

class Invoker:
    def __init__(self,order,bookList,invoice):
        self.__displayBookListCmd = DisplayBookListCommand(bookList)
        self.__submitOrderCmd = SubmitOrderCommand(order)
        self.__displayInvoiceCmd = DisplayInvoiceCommand(invoice)
    
    def displayBookList(self):
        self.__displayBookListCmd.execute()

    def submitOrder(self):
        self.__submitOrderCmd.execute()
    def displayInvoice(self):
        self.__displayInvoiceCmd.execute()
        

    def __init__(self):
        self.__commands = []

    def addCommand(self,command):
        self.__commands.append(command)

    def doWork(self):
        [c.execute() for c in self.__commands]


def main():
    book= Book()
    orderItem= OrderItem()
    order=Order()
    bookList= BookList()
    invoice= Invoice()
    
    invoker= Invoker()
    invoker.addCommand(DisplayBookListCommand(bookList))
    invoker.addCommand(SubmitOrderCommand(order))
    invoker.addCommand(DisplayInvoiceCommand(invoice))

    invoker.doWork()
main()