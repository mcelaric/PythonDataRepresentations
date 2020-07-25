# Question 1
# What slicing returns [5,7,9]
my_list = [1,3,5,7,9]

print(my_list[2:5])  # YES
print(my_list[2:])   # YES


# Question 2
# What returns a tuple of length 1?

print((1,))         # YES
print(tuple([1]))   # YES

# Question 3
# Why does following code snippet raise an error in Python?
# instructors = ("Scott", "Joe", "John", "Stephen")
# instructors[2 : 4] = []
# print(instructors)

# Answer - tuples are immutable
# TypeError: 'tuple' object does not support item assignment

# Question 4
# Given a non-empty list my_list, 
# which item in the list does the operation my_list.pop() remove?
print("pop operation", my_list.pop())

my_list = [1,3,5,7,9]
# Answer
print("index -1", my_list[-1])   

# Question 5
# What output does the following code snippet print to the console?
my_list = [1, 3, 5, 7, 9]
my_list.reverse()
print(my_list.reverse())
#None

"""
Given a list fib = [0, 1], write a loop that appends the sum of the last two items in
fib to the end of fib. 
What is the value of the last item in fib after twenty iterations of this loop? 
Enter the answer below as an integer.

As a check, the value of the last item in fib after ten iterations is 89.
"""

def append_sum(lst,n):
    for i in range(0,n):
        last_item = lst[-1]
        second_last_item = lst[-2]
        combined = last_item + second_last_item
        lst.append(combined)
    #return(lst)
    return lst.pop()

fib = [0,1]
print(append_sum(fib,20))

# Question 7
"""
One of the first examples of an algorithm was the Sieve of Eratosthenes. 
This algorithm computes all prime numbers up to a specified bound. 
The provided code below implements all but the innermost loop for this algorithm 
in Python. 
Review the linked Wikipedia page and complete this code.

Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Running your completed code should print two numbers in the console. 
The first number should be 46
"""
import math
primes = []
number = 200
for i in range(2,number+1):
    primes.append(i)

i = 200
#from 2 to sqrt(number)
while(i <= int(math.sqrt(number))):
    #if i is in list
    #then we gotta delete its multiples
    if i in primes:
        #j will give multiples of i,
        #starting from 2*i
        for j in range(i*2, number+1, i):
            if j in primes:
                #deleting the multiple if found in list
                primes.remove(j)
    i = i+1

print (primes)

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        # Remove appropriate multiples of divisor from answer
        pass
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))