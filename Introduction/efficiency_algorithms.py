# What is an Efficiency of algorithms
# The same task can be solved by different algorithms
# and there can be big differences in their efficiencies.
# Often the goal is to find an efficient algorithm that solves the task quickly.

# This function calculates the maximum absolute difference between any two numbers in the list

import random
import time

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

# Algorithm 3:
def max_diff_3(numbers):
    return max(numbers) - min(numbers)

n = 1000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = max_diff_2(numbers)
end_time = time.time()

print("result", result)
print("time:", round(end_time - start_time, 2), "s")