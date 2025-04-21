class MySet:
    def __init__(self):
        # Initialize an empty list to store set elements
        self.data = []
    
    def add(self, element):
        # Adds an element to the set if it's not already present
        if element not in self.data:
            self.data.append(element)
    
    def remove(self, element):
        # Removes an element from the set if it exists
        if element in self.data:
            self.data.remove(element)
    
    def contains(self, element):
        # Checks if an element exists in the set
        return element in self.data
    
    def size(self):
        # Returns the number of elements in the set
        return len(self.data)
    
    def intersection(self, other_set):
        # Returns a new set containing elements common in both sets
        result = MySet()
        for item in self.data:
            if item in other_set.data:
                result.add(item)
        return result
    
    def union(self, other_set):
        # Returns a new set containing all elements from both sets
        result = MySet()
        for item in self.data:
            result.add(item)
        for item in other_set.data:
            result.add(item)
        return result
    
    def difference(self, other_set):
        # Returns a new set with elements in self but not in other_set
        result = MySet()
        for item in self.data:
            if item not in other_set.data:
                result.add(item)
        return result
    
    def subset(self, other_set):
        # Checks if self is a subset of other_set
        for item in self.data:
            if item not in other_set.data:
                return False
        return True

# Example usage
s1 = MySet()
s1.add(1)
s1.add(2)
s1.add(3)

s2 = MySet()
s2.add(2)
s2.add(3)
s2.add(4)

print("Set 1:", s1.data)
print("Set 2:", s2.data)
print("Intersection:", s1.intersection(s2).data)
print("Union:", s1.union(s2).data)
print("Difference (s1 - s2):", s1.difference(s2).data)
print("Is s1 subset of s2?", s1.subset(s2))
