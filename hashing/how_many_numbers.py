# Task: You are given a list of numbers. How many distinct numbers does it contain?
import time
import random

# as a list
def count_distinct_list(numbers):
    seen = []
    for number in numbers:
        if number not in seen:
            seen.append(number)
    return len(seen)

def count_distinct_set(numbers):
    seen = set()
    for number in numbers:
        if number not in seen:
            seen.add(number)
    return len(seen)

def count_distinct_simplify(numbers):
    seen = set()
    for n in numbers:
        seen.add(n)
    return len(seen)

# count_distinct_list VS. count_distinct_set
# This change has a big effect on the efficiency of the algorithm.
large_list = [random.randint(0, 10000) for _ in range(1_000_000)]

start_time = time.time()
print("Distinct (list):", count_distinct_list(large_list))
end_time = time.time()
print("Time (list):", round(end_time - start_time, 2), "s")

# Testando a função com set
start_time = time.time()
print("Distinct (set):", count_distinct_set(large_list))
end_time = time.time()
print("Time (set):", round(end_time - start_time, 2), "s")