# Task: You are given a list of numbers, and your task is to compute the mode
# which is the most frequent number on the list. If the mode is not unique, you
# can choose any of the possible choices for the most frequent number.

def find_mode(numbers):
    count = {}
    mode = numbers[0]

    for number in numbers:
        if number not in count:
            count[number] = 0
        count[number] += 1

        if count[number] > count[mode]:
            mode = number
    return mode

print(find_mode([1,2,3,2,2,3,2,2]))