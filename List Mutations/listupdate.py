"""
Mutating Lists.
"""

print("Updating Items")
print("==============")

lst = list(range(5))
print("Original list",lst)

lst[1] = -7
lst[3] = 17
print("Altered list", lst)

print("")
print("Adding Items")
print("============")

lst.append(42)
print(lst)

lst.insert(2, 75)
print(lst)

print("")
print("Extending lists")
print("===============")
lst2 = [-56, 27, 8]
lst.extend(lst2)
print(lst)

print("")
print("Appending list as a whole to a list")
print("===================================")
lst.append(lst2)
print(lst)

print("")
print("Removing Items")
print("==============")

lst.pop()  # No args defaults to popping last item off list
print(lst)
lst.pop(3)
print(lst)