
from abc import ABC, abstractmethod


class Catalog_item(ABC):
    def __init__(self,catalog_number,title):
        self.__catalog_number = catalog_number
        self.__title = title

    @property
    def catalog_number(self):
        return self.__catalog_number

    @catalog_number.setter
    def catalog_number(self,catalog_number):
        self.__catalog_number = catalog_number

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        self.__title = title

    def display(self):
        pass

class Book(Catalog_item):
    def __init__(self, catalog_number, title,material):
        super().__init__(catalog_number, title)
        self.__material= material

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self,material):
        self.__material = material

class Movie(Catalog_item):
    def __init__(self, catalog_number, title,material,length_of_movie):
        super().__init__(catalog_number, title)
        self.__material= material
        self.__length_of_movie= length_of_movie

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self,material):
        self.__material = material

    @property
    def length_of_movie(self):
        return self.__length_of_movie

    @length_of_movie.setter
    def length_of_movie(self,length_of_movie):
        self.__length_of_movie = length_of_movie
class Magazine(Catalog_item):
    def __init__(self, catalog_number, title,material,articles,issue_date):
        super().__init__(catalog_number, title)
        self.__material = material
        self.__articles= articles
        self.__issue_date = issue_date
    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self,material):
        self.__material = material

    @property
    def articles(self):
        return self.__articles

    @articles.setter
    def articles(self,articles):
        self.__articles = articles

    @property
    def issue_date(self):
        return self.__issue_date

    @issue_date.setter
    def issue_date(self,issue_date):
        self.__issue_date = issue_date

class Artile(Magazine):
    def __init__(self, catalog_number, title, material, articles, issue_date,subject):
        super().__init__(catalog_number, title, material, articles, issue_date)
        self.__subject= subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self,subject):
        self.__subject = subject

class Library(Book,Movie,Magazine,):
    def __init__(self, catalog_number, title, material,books,magazines,movies):
        super().__init__(catalog_number, title, material)
        self.__books = []
        self.__magazines =[]
        self.__movies = []
    def addItem(self,item):
        self.__books.append(item)
        self.__magazines.append(item)
        self.__movies.append(item)

    def edit_information(self,catalog_number):
        pass
    def display(self):
        return super().display() 

class Person:
    def __init__(self,name,age):
        self.__name= name
        self.__age
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age
    
    def display():
        pass
    def displayRoles():
        pass
class Student(Person):
    def __init__(self, name, age,studentID,gpa):
        super().__init__(name, age)
        self.__studentID= studentID
        self.__gpa = gpa

    @property
    def studentID(self):
        return self.__studentID

    @studentID.setter
    def studentID(self,studentID):
        self.__studentID = studentID

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self,gpa):
        self.__gpa = gpa
    def display():
        pass
    def displayRoles():
        pass
class Teacher(Person):
    def __init__(self, name, age,specialty,salary):
        super().__init__(name, age)
        self.__specialty = specialty
        self.__salary = salary
    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self,specialty):
        self.__specialty = specialty
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        self.__salary = salary

    def display():
        pass
    def displayRoles():
        pass
class TA(Student,Teacher):
    def __init__(self, name, age, studentID, gpa,section):
        super().__init__(name, age, studentID, gpa)
        self.__section = section
    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self,specialty):
        self.__specialty = specialty
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        self.__salary = salary

    def display():
        pass
    def displayRoles():
        pass
def main():

    teacher=Teacher()
    teacher.name=" Henry "
    teacher.age =" 45 "
    teacher.salary= " 4000 "
    teacher.specialty = " Programming  "
    teacher.display()

main()
    

    



