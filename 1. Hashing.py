# Hash Table Implementation using Linear & Quadratic Probing


# Class Definition for Hash Table
class HashTable:
    def __init__(self):  
        """Constructor: Initializes the hash table with user-defined size."""
        self.m = int(input("Enter size of hash table: "))  
        self.hashTable = [None] * self.m  # Initializes hash table with None
        self.elecount = 0  # Counts number of elements inserted
        self.comparisons = 0  # Tracks number of comparisons during insertion/search
        print(self.hashTable)  # Prints initial empty hash table

    # Hash Function
    def hashFunction(self, key):
        return key % self.m

    # Check if Hash Table is Full
    def isFull(self):
        return self.elecount == self.m

    # Linear Probing Insert Method
    def linearProbingInsert(self, key, data):
        index = self.hashFunction(key)
        compare = 0

        # Find next available slot using linear probing
        while self.hashTable[index] is not None:
            index = (index + 1) % self.m
            compare += 1

        self.hashTable[index] = [key, data]
        self.elecount += 1
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"Number of comparisons: {compare}")

    # Linear Probing Search Method
    def linearProbingSearch(self, key, data):
        index = self.hashFunction(key)

        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            index = (index + 1) % self.m  # Linear probing to search for key

        return None  # Key not found

    # Quadratic Probing Insert Method
    def quadraticProbingInsert(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        i = 1

        while self.hashTable[index] is not None:
            index = (index + i * i) % self.m
            compare += 1
            i += 1

        self.hashTable[index] = [key, data]
        self.elecount += 1
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"Number of comparisons: {compare}")

    # Quadratic Probing Search Method
    def quadraticProbingSearch(self, key, data):
        index = self.hashFunction(key)
        i = 1

        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            index = (index + i * i) % self.m  # Quadratic probing for key search
            i += 1

        return None  # Key not found

    # Insert Using Linear Probing
    def insertUsingLinear(self, key, data):
        if self.isFull():
            print("Table is full")
            return False

        index = self.hashFunction(key)

        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print(f"Data inserted at index {index}")
            print(self.hashTable)
        else:
            print("Collision occurred! Applying Linear Probing...")
            self.linearProbingInsert(key, data)

    # Insert Using Quadratic Probing
    def insertUsingQuadratic(self, key, data):
        if self.isFull():
            print("Table is full")
            return False

        index = self.hashFunction(key)

        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print(f"Data inserted at index {index}")
            print(self.hashTable)
        else:
            print("Collision occurred! Applying Quadratic Probing...")
            self.quadraticProbingInsert(key, data)


# Menu for User Interaction
def menu():
    obj = HashTable()
    
    while True:
        print("\n************************")
        print("1. Linear Probing")
        print("2. Quadratic Probing")
        print("3. Exit")
        print("************************")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            while True:
                print("\n1. Insert")
                print("2. Search")
                print("3. Back to Main Menu")
                ch2 = int(input("Enter your choice: "))

                if ch2 == 1:
                    a = int(input("Enter phone number: "))
                    b = input("Enter name: ")
                    obj.insertUsingLinear(a, b)
                elif ch2 == 2:
                    k = int(input("Enter key to search: "))
                    b = input("Enter name: ")
                    f = obj.linearProbingSearch(k, b)
                    if f is None:
                        print("Key not found")
                    else:
                        print(f"Key found at index {f}")
                elif ch2 == 3:
                    break  # Go back to main menu

        elif ch == 2:
            obj1 = HashTable()

            while True:
                print("\n1. Insert")
                print("2. Search")
                print("3. Back to Main Menu")
                ch2 = int(input("Enter your choice: "))

                if ch2 == 1:
                    a = int(input("Enter phone number: "))
                    b = input("Enter name: ")
                    obj1.insertUsingQuadratic(a, b)
                elif ch2 == 2:
                    k = int(input("Enter key to search: "))
                    b = input("Enter name: ")
                    f = obj1.quadraticProbingSearch(k, b)
                    if f is None:
                        print("Key not found")
                    else:
                        print(f"Key found at index {f}")
                elif ch2 == 3:
                    break  # Go back to main menu

        elif ch == 3:
            print("Exiting program...")
            break

# Run the program
menu()
