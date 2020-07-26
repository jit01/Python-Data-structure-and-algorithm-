from abc import ABC, abstractmethod


class Parent(ABC):

    @abstractmethod
    def money(self):
        """
        @abstractmethod determine money method must be implemented in base class
        otherwise it will return the error
        """
        print("Must be implemented in base class ")


class Child(Parent):

    def wife(self):
        print("Child have wife")

    def money(self):
        print("Yes, Your child have enough money")


c = Child()
print(c.wife())
print(c.money())
