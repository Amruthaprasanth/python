
from abc import ABC,abstractmethod

class Vehicle(ABC):
    def start_engine(self):
        print("start engine")
    def apply_break(self):
        print("applying break")
    def stop_engine(self):
        print("stopping engine")
    @abstractmethod
    def change_gear(self):
        pass    
class Car(Vehicle):
    def open_sunroof(self):
        print("opening sunroof")
    def change_gear(self):
        print("change gear automatically")    
class Truck(Vehicle):
    def load_weight(self):
        print("loading weight")
    def change_gear(self):
        print("change gear manually")    
c=Car()
t=Truck()
c.change_gear()
t.change_gear()
