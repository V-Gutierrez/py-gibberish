# OOP

# "A Car is a thing that runs and has a name."
#
# The class is called Car. It has two methods: __init__ and start. The __init__ method is a special
# method that is called when you create a new instance of the class. The start method is a normal
# method that you can call on an instance of the class
class Car:
    runs = True

    def __init__(self) -> None:
        print("New Car")
        self.start("BMW")

    def __str__(self) -> str:
        return f"Car {self.name} is running and this is the string representation of it"

    def __repr__(self) -> str:
        return f"Car({self.name})"

    def start(self, name: str) -> None:  # Type hinting
        self.name = name

    @classmethod
    def get_runs(cls) -> bool:
        return cls.runs


car = Car()

print(str(car))

# [run it for item in items]
x = [1, 2, 3, 4, 5]
y = [float(item) for item in x]

print(y)


