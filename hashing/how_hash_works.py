# The Python data structures of this chapter, set and dict, are based on hashing and a data structure called the hash table.
# In python, a hash table is implemented using open hashing.

print(hash(10**100))
print(hash("password"))

# Which objects can be hashed?
# lists = set()
# list.add([1,2,3]) # TypeError: unhashable type: 'list'
# print(hash([1,2,3])) # TypeError: unhashable type: 'list'

lists = set()
lists.add((1,2,3))

class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
        

locations = set()
locations.add(Location(1, 2))
locations.add(Location(3, -5))
locations.add(Location(1, 4))

print(locations)