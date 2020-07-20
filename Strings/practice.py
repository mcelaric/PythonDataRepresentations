"""
Template - String examples
"""

# Fix the four string definitions below.

string1 = "It's just a flesh wound"
string2 = "It's just a flesh wound"    
string3 = "It's just a flesh wound"    
string4 = """It's just a flesh wound"""

print(string1)
print(string2)
print(string3)
print(string4)

"""
Template - Item selection for lists
"""

# Create a string formed by selecting the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[0] + example_string[-1] 
print(solution_string)

# Output should be 
#It's just a flesh wound
#Id

"""
Template - Slice selection for lists
"""

# Create a string formed by selecting all but the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[1:-1] 
print(solution_string)

# Output should be 
#It's just a flesh wound
#t's just a flesh woun

"""
Template - Echo a string multiple times to the console
"""

def echo(call, repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    """
    #print_string = call + "\n"
    #print(print_string * repeats)
    # Solution
    answer = call + ('\n' + call) * (repeats - 1)
    print(answer)    


# Tests
echo("Hello", 5)
echo("Goodbye", 3)

# Output
#Hello
#Hello
#Hello
#Hello
#Hello
#Goodbye
#Goodbye
#Goodbye


"""
Template - Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    # Enter code here
    first, last = name_string.split(" ")
    swapped = last + " " + first
    return swapped
    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))


# Output

#Warren Joe
#Rixner Scott
#Greiner John