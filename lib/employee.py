class Employee:
    __id = 0
    def __init__(self, id, first, last, age, salary): 
        self.__id += 1
        self.__first = first
        self.__last = last
        self.__age = age
        self.__salary = salary

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, first):
        self.__first = first

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, last):
        self.__last = last

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

