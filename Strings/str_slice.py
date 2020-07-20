"""
Slicing strings.
"""

word = "everything"
print("The word to slice - ", word)
# Selecting substrings
print("Slicing word[1:5] - ", word[1:5])
print("Slicing word[5:9] - ", word[5:9])

# Open ended slices
print("Slicing word[5:] - ", word[5:])
print("Slicing word[:4] - ", word[:4])

# Using negative indices
print("Slicing word[-3:] - ", word[-3:])
print("Slicing word[2:-3] - ", word[2:-3])

# Indexing past the end
print("Slicing word[8:20] - ", word[8:20])
print("$" + word[22:29] + "^")

# Empty slices
print("Slicing word[6:6] - ", word[6:6])
print("Slicing word[4:2] - ", word[4:2])