pets = ["cat", "dog", "ferret"]

for animal in pets:
    print(animal)


numbers = [3, 8, -2, 4, 13]
sumsq = 0

# Sum all the squares of the numbers in 'numbers'
for num in numbers:
    square = num * num
    sumsq += square
    
print(sumsq)

    
def list_minimum(numbers):
    """
    Compute the minimum of a list of numbers
    """
    
    min_num = float("inf")
    for num in numbers:
        if num < min_num:
            min_num = num  # Set "Run to cursor" on this line
    return min_num

def run_example():
    """
    Run an example using list_minimum
    """
    example_list = [4.6, 5.9, 2.1, 5.7, 1.1, 8.3]
    print("An example list is", example_list)
    print()
    minimum_number = list_minimum(example_list)
    print("The minimum of this example list is", minimum_number)

run_example()    