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
# import math
# primes = []
# number = 2000
# for i in range(2,number+1):
#     primes.append(i)
# 
# i = 2
# #from 2 to sqrt(number)
# while(i <= int(math.sqrt(number))):
#     #if i is in list
#     #then we gotta delete its multiples
#     if i in primes:
#         #j will give multiples of i,
#         #starting from 2*i
#         for j in range(i*2, number+1, i):
#             if j in primes:
#                 #deleting the multiple if found in list
#                 primes.remove(j)
#     i = i+1
# 
# print (len(primes))

"""
PROVIDED ANSWER AFTER QUIZ SUBMISSION!!!
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        for stride in range(2 * divisor, bound, divisor):            
            if stride in answer:
                answer.remove(stride)
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))
