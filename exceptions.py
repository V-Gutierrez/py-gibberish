class MyCustomException(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

        super().__init__(error_message)


try:
    x = input("Enter a number: ")
    int(x)
except ValueError:
    raise MyCustomException("You did not enter a number")
