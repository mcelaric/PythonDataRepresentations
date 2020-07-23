"""
List Literals
"""

lst1 = [1, 5, 9, -32]
print(lst1)

lst2 = ["dog", "cow", "horse"]
print(lst2)

emptylst = []
print(emptylst)

"""
Range & List Indexing
"""

lst = list(range(10))

# First element
print(lst[0])

# Third element
print(lst[2])

# Length
print(len(lst))

# Last element
print(lst[9])
print(lst[len(lst) - 1])
print(lst[-1])

"""
List Slicing
"""

lst = list(range(10))

# Slice with 3 elements
print(lst[4:7])

"""
Negative indices may be used in slicing, and they have exactly the same meaning that they did when 
used as indices. You can even mix positive and negative indices in a slice.
"""
# Slice with the last 2 elements of the list
print(lst[8:10])
print(lst[8:])
print(lst[-2:])

# Slice with the first 4 elements of the list
print(lst[0:4])
print(lst[:4])

"""
Rather than causing errors, if there are no elements in the list between the indices in the slice, 
then an empty list is produced.
"""
# Empty slices
print(lst[20:25])
print(lst[7:3])