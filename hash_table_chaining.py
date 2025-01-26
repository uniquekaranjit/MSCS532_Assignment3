# ----------------------------------------------------------------------------------------------------------------------
# Driver Code to analyze and compare randomized quicksort with deterministic quick sort (first element as pivot) 
# Author: Unique Karanjit
# Jan 25, 2025
# ----------------------------------------------------------------------------------------------------------------------
import random

class HashTable:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]
        # Choose a large prime number for p
        self.p = 2**31 - 1  # A large prime number
        # Randomly choose a and b
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    # Universal hash function
    def hash(self, key):
        # Convert key to a string and then to its hash value
        key_bytes = str(key).encode('utf-8')
        key_hash = sum(key_bytes)  # Use sum of bytes as a simple hash
        # Universal hash formula
        return ((self.a * key_hash + self.b) % self.p) % self.capacity

    # Insert operation
    def insert(self, key, value):
        index = self.hash(key)
        # Check if the key already exists, and update its value
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If the key is not found, add a new key-value pair
        self.table[index].append((key, value))

    # Search operation
    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    # Delete operation
    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False  # Key not found

    # For testing
    def display(self):
        for index, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {index}: {bucket}")

# ----------------------------------------------------------------------------------------------------------------------
# Driver Code
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    hash_table = HashTable()

    # Insert some entries
    hash_table.insert("LexusMake", "Lexus")
    hash_table.insert("AcuraMake", "Acura")
    hash_table.insert("ToyotaMake", "Toyota")
    hash_table.insert("BMWMake", "BMW")
    hash_table.insert("AudiMake", "Audi")
    hash_table.insert("TeslaMake", "Tesla")

    # Display the table
    print("\n\n---------------------------------------")
    print("Showing the Table")
    print("---------------------------------------")
    hash_table.display()

    # Search for an entry
    print("\n\n---------------------------------------")
    print("Searching for entries LexusMake and AcuraMake from the Table")
    print("---------------------------------------")
    print("Make:", hash_table.search("LexusMake")) 
    print("Make:", hash_table.search("AcuraMake"))    

    # Delete an entry
    print("\n\n---------------------------------------")
    print("Deleting entry ToyotaMake the Table")
    print("---------------------------------------")
    print("Deleted Make:", hash_table.delete("ToyotaMake"))  # Output: True

    print("\n\n---------------------------------------")
    print("Searching entry ToyotaMake the Table after deletion")
    print("---------------------------------------")
    print("After Deletion:: Make:", hash_table.search("ToyotaMake"))  # Output: None

    # Display the table after deletion
    print("\n\n---------------------------------------")
    print("Showing the Table")
    print("---------------------------------------")
    hash_table.display()
    print("\n\n\n\n")
