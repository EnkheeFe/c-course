#presentation layer
from Db import CustomerData
from Business import Customer,CustomerLists, Employee, Manager

class BankApp:
    def __init__(self):
        customerdb = CustomerData()
        self.__customers = customerdb.getClients()
        self.__employee = Employee()

    def showTitle(self):

        print("The Bank Application program")

        print()

    def showMenu(self):

        print("Command Menu")
        print("add - Add a new customer to customer lists")
        print("del - Delete a customer from customer lists")
        print("print - Print customer lists")
        print("exit - Exit program")

        print()

    def showCustomers(self):
        print("Customers")
        lineFormat1 = "{:<5s}{:<25s}{:>25s}{:>10s}"
        lineFormat2 = "{:<5s}{:<25s}{:>25s}{:>10s}"
        print(lineFormat1.format("Firstname","Lastname","Accountnumber","Balance"))
        print(lineFormat2.format(Customer.firstName,Customer.lastName,Customer.accountNumber,Customer.accountBalance))

        print

def main():
    app = BankApp()
    app.showTitle()
    app.showMenu()
    #display Customer objects
    app.showCustomers()

    while True:
        command = input("Command:")
        if command == "add":
            app.addCustomer()
        elif command == "del":
            app.delCustomer()
        elif command == "print":
            app.showCustomers()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

    if__name__== "__main__":
        main()

            


    