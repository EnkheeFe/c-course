# data layer
import csv
from Business import Customer

class CustomerData:

    def __init__(self):
        self.__FileName = "customerLists.csv"

    def getClients(self):
        customers={}

        with open(self.__FileName,newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                # convert row to Customer object

                customer = Customer(row[0],row[1],row[2])

                customers[row[0]] = customer
        return customers
