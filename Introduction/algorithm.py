# What is an algorithm?
# An algorithm is a method for solving some computational problem.
# An algorithm implemented in some programming language can be executed on a computer.

def count_even(numbers):
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result += 1
    return result
    

numbers = 0
for i in range(0,5):
    numbers += 1
