"""
Template- Create a list of the first six primes and print the 2nd, 4th, and 6th
"""

# Enter code here
primes = [2, 3, 5, 7, 11, 13]
print(primes[1], primes[3],primes[5])
    

# Output
#3 7 13

"""
Template - Create a list formed by 8 copies of True and 8 copies of False
"""

# Uncomment and enter code here

truefalse_list = 8 * [True] + 8 * [False] 
print(truefalse_list)


# Output
#[True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False]


"""
Template - Create a list of words form a string consisting of words separated by spaces
"""

# Uncomment and enter code here

quote = "Bring me a shrubbery"
word_list = quote.split()
print(word_list)


# Output
#['Bring', 'me', 'a', 'shrubbery']

"""
Template - Take a list of integers and concatenate their digits
"""

def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    digits = ""
    for number in int_list:
        digits += str(number)
    return int(digits)

# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))


# Output
#4
#404
#123456789
#327961000