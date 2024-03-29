"""
List creation.
"""

print("List Literals")
print("=============")

# List literals
empty = []
print("empty - ", empty)

numbers = [1, 5, 8, 3, 2]
print("numbers - ", numbers)

letters = ["a", "z", "c", "q", "c", "a"]
print(letters)

languages = ["python", "java", "javascript", "lisp", "c++", "haskell"]
print("languages - ",languages)

# Don't mix types in a list!
mixed = ["a", 1, True]
print("mixed - ", mixed)

print("")
print("Creating Lists")
print("==============")

mylist = list()
print("mylist - ", mylist)

seq = range(5)
print("seq - ", seq)

seqlst = list(seq)
print("seqlst - ", seqlst)

seq2 = range(7, 13)
print(seq2, list(seq2))

seq3 = range(4, 27, 5)
print(seq3, list(seq3))

seq4 = range(9, 2, -1)
print(seq4, list(seq4))