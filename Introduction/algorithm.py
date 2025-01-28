# What is an algorithm?
# An algorithm is a method for solving some computational problem.
# An algorithm implemented in some programming language can be executed on a computer.

def count_even(numbers):
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result += 1
    return result

print(count_even([1, 2, 3])) # 1
print(count_even([2, 2, 2, 2, 2])) # 5
print(count_even([5, 4, 1, 7, 9, 6])) # 2