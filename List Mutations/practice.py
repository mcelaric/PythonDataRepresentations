"""
Template - Update an item in a list
"""

example_list = [2, 3, 5, 7, 11, 13]
example_list[2] = 0
print(example_list)

# Enter update code here

#print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 0, 7, 11, 13]

"""
Template - Update a slice of a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
new_list = [0,0,0]
example_list[1:3] = new_list
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 0, 0, 0, 7, 11, 13]

"""
Template - Concatenate one list onto another
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
new_list = list(example_list) + [0,0,0]
          
print(example_list)
print(new_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]


"""
Template - Flatten a nested list
"""

def flatten(nested_list):
    """
    Given a list whose items are list, 
    return the list formed by joining all of these lists
    """
    # Given solution
#     for sub_list in nested_list:
#         flattened_list.extend(sub_list)    
    
    flattened_list = []
    for item in flattened_list:
        rtn_lst = rtn_lst + item
    return flattened_list

# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]