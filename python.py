def greeting(name):
    """
    It prints out a greeting to the person whose name is passed in as an argument.

    :param name: This is the name of the person you want to greet
    """
    print(f"Hello, world! {name}")


greeting("Victor")

lottery_numbers = list([1123441, 23, 4124, 523523, 1239912])

print(lottery_numbers)

print(f"This is the sorted version {sorted(lottery_numbers)}")

print(lottery_numbers.count(1123441))

# Tuples (Related but different items)
# Once create ~ immutable

my_first_tuple = (1, 2, 3, 4, 5)

print(type(my_first_tuple))

students = ("Victor", "M", "CS", 9.7)

name, gender, subject, gpa = students  # Unpacking aka destructuring

print(name, gender, subject, gpa)


def http_status_code():
    """
    It returns the HTTP status code of the response as a tuple.
    """
    return 200, 'OK'  # This is returning a tuple


print(http_status_code())

code, status = http_status_code()  # This is possible


# SETS
# Sets are a datatype that allows you to store other immutable types in an unsorted way. An item can only be contained in a set once. There are no duplicates allowed. The benefits of a set are: very fast membership testing along with being able to use powerful set operations, like union, difference, and intersection.

my_first_set = set()

my_first_set.add(1)  # You cant add unhashable types like lists and dicts

print(my_first_set, 1 in my_first_set)  # {1} True

# discard wont throw an error if the item is not in the set
my_first_set.remove(1)

print(my_first_set, 1 in my_first_set)  # set() False


rainbown_colors = {"blue", "green", "yellow", "red", "orange", "purple"}

favorite_colors = {"blue", "black"}

# {'yellow', 'red', 'orange', 'purple'}
rainbown_colors.difference(favorite_colors)

print(rainbown_colors.difference(favorite_colors))
print(rainbown_colors.union(favorite_colors))  # black is added

# intersection
intersect = rainbown_colors & favorite_colors
union = rainbown_colors | favorite_colors
difference = rainbown_colors ^ favorite_colors

print(intersect, union, difference)

list_from_set = list(rainbown_colors)

print(list_from_set, type(list_from_set))


# DICTIONARIES
# Mutable ~ Keys are immutable type and values are any mutable/immutable type

# or dict() (looks alike Map in JS)
my_first_dict = {"1": "Hello dict", None: 2, False: 3, True: 4}

print(my_first_dict, my_first_dict["1"], my_first_dict[None])

my_first_dict[None] = '0'

print('0' in my_first_dict)  # False because it checks the keys no the values
print(None in my_first_dict)  # True

my_second_dict = {"new item": 22222}

my_first_dict.update(my_second_dict)
print(my_first_dict)  # new item is there


# ---

my_new_list = ['h', 'e', 'l', 'l', 'o']

print(my_new_list[0:3])  # ['h', 'e', 'l']
print(my_new_list[0:4])  # ['h', 'e', 'l', 'l']
print(my_new_list[0:5])  # ['h', 'e', 'l', 'l', 'o']


print(bool(my_new_list))

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # shallow comparison equality
print(a is b)  # deep comparison identity


t_a = a or 1

print(a)


# Loops

for items in a:
    print(f"{items} is an item of the list")

new_new_list = list(range(0, 2000, 1000))

print(new_new_list)


for item in my_first_dict:
    print(f"{item} is an item of the dict")

for key, value in my_first_dict.items():
    print(f"{key} is an item of the dict with value {value}")
