# What is an Efficiency of algorithms
# The same task can be solved by different algorithms
# and there can be big differences in their efficiencies.
# Often the goal is to find an efficient algorithm that solves the task quickly.

# This function calculates the maximum absolute difference between any two numbers in the list

# Algorithm 1:
def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x - y))
    return result

# Algorithm 2:
def max_diff_2(numbers):
    # Order the numbers
    numbers = sorted(numbers)

    # Take the last (largest) number and subtract it from the first (smallest) number in the ordered list.
    return numbers[-1] - numbers[0]

print(max_diff_2([3, 2, 6, 5, 8, 5]))