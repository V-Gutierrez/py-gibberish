not_a_generator = [1, 3, 4, 5, 6, 7, 8, 9, 10]

# Creating a generator object.
# return x for x in not_a_generator
a_legit_generator = (x for x in not_a_generator)
# each item is lazily evaluated


print(not_a_generator, type(not_a_generator),
      a_legit_generator, type(a_legit_generator))
