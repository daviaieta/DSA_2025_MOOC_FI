# Task: You are given a bit string consisting of the characters 0 and 1.
# How many ways can you select two positions in the bit string so that
# the left position contains the bit 0 and the right position contains the bit 1?

# The algorithm is too slow as its time complexity
def count_ways_slow(bits):
    n = len(bits)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bits[i] == "0" and bits[j] == "1":
                result += 1
    return result

# Best way with no complexity
def count_ways(bits):
    result = 0
    zeros = 0
    for i in range(len(bits)):
        if bits[i] == "0":
            zeros += 1
        if bits[i] == "1":
            result += zeros
    return result


bit_string = "01001011"
print(count_ways(bit_string))