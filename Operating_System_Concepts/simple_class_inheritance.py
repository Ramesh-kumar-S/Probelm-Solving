from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def print_description(self):
        pass


class Car(Vehicle):
    def print_description(self):
        print(f'Ramesh Own\'s and KIA Seltos')


class Plane(Vehicle):
    def print_description(self):
        print(
            f'Private Plane is owned by an Computing Engineer called "Ramesh Kumar Sekar"')


P = Plane()
P.print_description()
