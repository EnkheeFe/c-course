# banking system with 3 layers
#business layer


class Customer:
    def __init__(self,firstName,lastName,accountNumber,accountBalance):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accounNumber = accountNumber
        self.__accounBalance = accountBalance
    
    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self,firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def firstName(self,lastName):
        self.__lastName = lastName

    @property
    def accountNumber(self):
        return self.__accountNumber
    @accountNumber.setter
    def accountNumber(self,accountNumber):
        self.__accountNumber = accountNumber

    @property
    def accountBalance(self):
        return self.__accountBalance
    @accountBalance.setter
    def accountBalancer(self,accountBalance):
        self.__accountBalance = accountBalance

class Employee:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    def addInformation(self,firstName,lastName,accountNumber,accountBalance):
        firstname = str(input("enter firstname:"))
        lastname = str(input("enter lastname:"))
        accountnumber = str(input("enter accountnumber: "))
        accountbalance = str(input("enter accountbalance:"))
        self.__customerLists.append(firstname,lastname,accountnumber,accountbalance)

    
    def viewInformation(self,customerLists):
        for customers in customerLists:
            print(customers)

    def editInformation(self,customerLists):
        self.__customerLists=customerLists
        return

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name);
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        self.__salary = salary

    def printListofClients(self):
        print("CustomerLists:",self.__customerLists)
    def searchInformation(self):
        
    


    

    
    