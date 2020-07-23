# Question 1

# print(list(range(0,5)))
# print(list(range(0,5,1)))

print(list(range(0,6)))
print(list(range(6)))


# Question 2
my_list = ["This", "course", "is", "great"]

print("length of my_list is ", len(my_list) ) #4

# What non-negative index will print "great"
print(my_list[3])


# Question 3
# Split my_list into two halves

# NO
# my_list[0:len(my_list) // 2 - 1] AND my_list[len(my_list) // 2 : len(my_list)]
# my_list[0:len(my_list) // 2] AND my_list[len(my_list) // 2 + 1: len(my_list)]

# YES
# my_list[0:len(my_list) // 2] 
#AND 
# my_list[len(my_list) // 2 : len(my_list)]

# my_list[len(my_list) // 2 : len(my_list)] 
#AND 
# my_list[len(my_list) // 2 : ]

# my_list[:len(my_list) // 2] 
#AND 
# my_list[len(my_list) // 2 : ]



split1 = my_list[:len(my_list) // 2]
split2 = my_list[len(my_list) // 2 : ]
print(my_list)
print(split1, split2)
# 
# # Question  4
# 
# n = 3
# m = 3
# init_list = list(range(1, n))
# final_list = init_list * m
# print((n-1)*m)
# print(len(final_list))

# Answer is (n-1)*m

# Question 5 

# f nn is a non-negative integer, consider the list
# split_list computed by the code snippet below.
n = 12
test_string = "xxx" + " " * n + "xxx"
split_list = test_string.split(" ")
print(n + 1)
print(len(split_list))

# Answer is n + 1

# Question 6
# Select the code snippets below in which list2 is a copy of list list1 
# (as opposed to simply being another reference to the list list1).

# YES
#list1 = list(range(1, 10))
#list2 = [] + list1

#list1 = list(range(1, 10))
#list2 = list(list1)

#list1 = list(range(1, 10))
#list2 = list1[:]

# NO
#list1 = list(range(1, 10))
#list2 = list1


# Question 7
"""
Write a function strange_sum(numbers) that takes a list of integers 
and returns the sum of those items in the list that are not divisible by 3. 
When you are done, test your function using the code snippet below.
"""

def strange_sum(numbers):
    strange_sum = 0
    for num in numbers:
        if num % 3 != 0:
            strange_sum += num
            
    return strange_sum

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))















