"""
Some simple examples of reference issues for lists
"""

# Part 1 - references to two distinct objects
iipp1_instructors = ["Joe", "Scott", "John", "Stephen"]
iipp2_instructors = ["Joe", "Scott", "John", "Stephen"]
print(iipp1_instructors)
print(iipp2_instructors)

# Mutate one of the two objects
print("")
print("Pop from list 2")
print("===============")
iipp2_instructors.pop()
print(iipp1_instructors)
print(iipp2_instructors)
print()


# Part 2 - two references to the same object
print("")
print("list 2 refs list1")
print("=================")
iipp1_instructors = ["Joe", "Scott", "John", "Stephen"]
iipp2_instructors = iipp1_instructors
print(iipp1_instructors)
print(iipp2_instructors)

# Mutate the object
print("")
print("Pop ref to list 2")
print("===============")
iipp2_instructors.pop()
print(iipp1_instructors)
print(iipp2_instructors)
print()


# Part 3 - two references to an object and a copy of the object
print("")
print("list 2 a copy of list1")
print("======================")
iipp1_instructors = ["Joe", "Scott", "John", "Stephen"]
iipp2_instructors = list(iipp1_instructors)
print(iipp1_instructors)
print(iipp2_instructors)


# Mutate the one of the objects
print("")
print("Pop from list 2")
print("===============")
iipp2_instructors.pop()
print(iipp1_instructors)
print(iipp2_instructors)


