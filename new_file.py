def upper_case_name(name):
    """
    It returns the name in upper case.
    """
    return name.upper()


if __name__ == '__main__':
    name = "victor"

    print(upper_case_name(name))


try:
    int("a")
except ValueError as error:
    print(f"OOps! {error}")
