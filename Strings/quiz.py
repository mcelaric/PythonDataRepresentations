# Print last character of "shrubbery"
#print("shrubbery"[len("shrubbery") - 1])
#print("shrubbery"[-1])
print("Grail"[-1])
print("Grail"[4])

# Slice "dog" from "pigdog"
#print("pigdog"[3:6])
#print("pigdog"[3:])
print("Castle Anthrax"[7:])
print("Castle Anthrax"[7:15])


# What can NOT be used with strings in Python
# -
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
#s1 = "this"
#s2 = "is"
#s3 = s1 - s2

# What does the expression 
# a_str.index(sub) do when the string sub is not a substring of the string a_str?
a_str = "Some string"
sub = "shit"
#ndx = a_str.index(sub)
# Output - ValueError: substring not found

# Which of the string format expressions below return the string "abracadabra"?
print("{}{}{}".format("abra", "cad", "abra"))
print("{0}{1}{0}".format("abra", "cad"))
print("{2}{1}{0}".format("abra", "cad", "abra"))

"""
Write a function count_vowels(word) 
    that takes the string word as input 
    returns the number of occurrences of lowercase vowels (i.e. the lowercase letters "aeiou") in word. 
    Hint: Python has a built-in string method that can count the number of occurrences of a letter in a string.
"""
def count_vowels(word):
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")  
    
# Example returns 13    
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))  

# This returns 17
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

"""
Write a function demystify(l1_string) that takes a string composed of the characters "l" and "1" 
and returns the string formed by replacing each instance of "l" by "a" 
and each instance of "1" by "b".
"""
def demystify(l1_string):
    rtn_string = l1_string.replace("l", "a")
    rtn_string = rtn_string.replace("1", "b")
    return rtn_string

print(demystify("lll111l1l1l1111lll"))

# prints "bbbababbabbaaabaaabaaabbbbbaabbabaababbb" 
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))