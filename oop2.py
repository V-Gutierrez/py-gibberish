class Vehicle:
    def __init__(self, make, model, fuel="gas") -> None:
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):  # Car extends Vehicle
    def __init__(self, make, model, fuel="gas", number_of_wheels=4) -> None:
        super().__init__(make, model, fuel)  # Call the parent class's constructor
        self.number_of_wheels = number_of_wheels

