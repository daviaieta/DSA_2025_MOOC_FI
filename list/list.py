# List operations

numbers = [4, 3, 7, 3, 2, 10, 9, 12]

# Indexing:
print(numbers[2]) # 7
print(numbers[0]) # 4

# List size:
print(len(numbers)) # 7

# Searching:
print(3 in numbers) # True
print(1 in numbers) # False

print(numbers.index(3)) # 1
print(numbers.index(9)) # 5 

# Adding an element
numbers.append(6)
numbers.insert(1,9)
print(numbers)

# Removing an element
numbers.pop()
numbers.pop(1)

# References and copying
a = [1, 2, 3, 4, 5, 6]
b = a

# For copying the contents, we can use the method copy:
b = a.copy()