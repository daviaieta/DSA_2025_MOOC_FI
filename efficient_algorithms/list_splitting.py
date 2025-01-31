# You are given a list containing n integers.
# Your task is to count how many ways one can split
# the list into two parts so that both parts have the same total sum of elements.

def count_splits(numbers):
    total_sum = sum(numbers)
    left_sum = 0
    result = 0

    for i in range(len(numbers) -1):
        left_sum += numbers[i]
        print(left_sum)
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            result += 1
    return result


print(count_splits([1, 1, 1, 1, 2, 2])) 
