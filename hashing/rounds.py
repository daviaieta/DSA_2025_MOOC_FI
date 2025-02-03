# Task: You are given a list that contains the numbers 1,2.. n in some order.
# Your task is to collect all the numbers in order from smallest to largest so
# that in each round you go through the list from left to right. How many rounds do you need?

# Slow solution(list)
def count_rounds(numbers):
    n = len(numbers)

    rounds = 1
    for i in range(1,n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1
    return rounds


# Efficient solution (dictionary)
def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1,n):
        if pos[i + 1] < pos[i]:
            rounds += 1
    return rounds