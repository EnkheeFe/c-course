from abc import ABC, abstractmethod
import enum

class Subject(ABC):
    @abstractmethod
    def registerObserver(self,o):
        pass
    @abstractmethod
    def removeObserver(self,o):
        pass
    @abstractmethod
    def notifyObserver(self):
        pass
class Observer(ABC):
    @abstractmethod
    def update(self,data):
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass



class House(Displayable):
    def __init__(self, address, squareFeet, numRooms, price):
        self.__address = address
        self.__squareFeet = squareFeet
        self.__numRooms = numRooms
        self.__price = price

    # add some public properties here if necessary 

    def display(self):
        print("Address=",self.__address,"," +"Square Feet=", self.__squareFeet,"," + "Num of Rooms=",self.__numRooms,","+"Price=",self.__price)


class Contact(Displayable):
    def __init__(self, firstName, lastName, phoneNumber, email):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__email = email
        self.__phoneNumber = phoneNumber

    # add some public properties here if necessary 

    def display(self):
        print('Last Name =',self.__lastName,"," +"First Name=",self.__firstName,","+"Phone Number=",self.__phoneNumber,","+"Email=",self.__email)


class Owner(Observer,Contact,ABC):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses = []
    

    def addHouse(self, house):
        self.__houses.append(house)

    def display(self):
        pass


class Buyer(Observer,Contact):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__watchList = []

    @property
    def watchList(self):
        return self.__watchList

    #  Save the house in his watch list 
    def saveForLater(self, house):
        self.watchList.append(house)

    # Remove the house from his watch list
    def removeFromSaveForLater(self, house):
        self.watchList.pop(house)

    def display(self):
        pass


class Company(Subject,Displayable):
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__owners = []
        self.__buyers = []
        self.__agents = []
        self.__houses = []
        self.__observers = []
    def registerObserver(self, o):
        self.__observers.append(o)
    def removeObserver(self, o):
        i = self.__observers.index(o)
        if i >= 0:
            self.__observers.pop(i)


    def addOwner(self, owner):
        self.__owners.append(owner)

    def addBuyer(self, buyer):
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def addAgent(self, agent):
        if agent not in self.__agents:
            self.__agents.append(agent)

    def addHouseToListing(self, house):
        self.__houses.append(house)
        self.notifyObserver(self)
    def getHouseByAddress(self, address):
        self.__houses.append(address)

    def removeHouseFromListing(self, house):
        self.__houses.pop(house)
        self.notifyObserver(self)
    # Help to remove that house from all buyers' watch list.
    def removeHouseFromSaveForLater(self, house):
        self.watchList.pop(house)

    def getBuyersByHouse(self, house):
        pass
    
    def notifyObserver(self,data):
        for o in self.__observers:
            o.update(data)
            print()
    

    def display(self):
        pass
       

class Agent(Observer,Contact):
    def __init__(self, lastName, firstName, phoneNumber, email, position, company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position = position
        self.__company = company

    def addHouseToListingForOwner(self, owner, house):
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)

    def helpBuyerToSaveForLater(self, buyer, house):
        self.__company.addBuyer(buyer)
        if self.__company.getHouseByAddress(house.address) is not None:
            buyer.saveForLater(house)
        else:
            print('Could not find your dream house but we kept your information first!')

    def editHousePrice(self, address, newPrice):
        pass

    def soldHouse(self, house):
        pass

    # print all potential buyers who are interested in buying that house
    def printPotentalBuyers(self, house):
        print(self.__company.addBuyer(house))

    def display(self):
        pass


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000)

    owner1.addHouse(house1)
    owner2.addHouse(house2)
    owner2.addHouse(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    agent1.addHouseToListingForOwner(owner1, house1)
    agent1.addHouseToListingForOwner(owner2, house2)
    agent1.addHouseToListingForOwner(owner2, house3)

    agent1.helpBuyerToSaveForLater(buyer1, house1)
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    agent1.editHousePrice('2222 Mission Blvd', 1200000)

    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.printPotentalBuyers(house1)



if __name__ == "__main__":
    main()