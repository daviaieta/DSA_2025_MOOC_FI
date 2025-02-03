# The Python data structure dict or dictionary is based on hashing and stores key-value pairs.
# The idea is that we can use the key to retrieve the associated value.

weights = {}

weights["banana"] = 100
weights["apple"] = 50
weights["strawberry"] = 50
print(weights)

print(weights["apple"]) # 50
weights["apple"] = 75
print(weights["apple"]) # 75

print("banana" in weights) # True
print("grape" in weights) # False

del weights['strawberry']
print(weights)