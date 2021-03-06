#Hashtable practice from Udacity course "Data Structures and Algorithms in Python"

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        location = self.calculate_hash_value(string)
        if self.table[location] != None:
            self.table[location].append(string)
        else: 
            self.table[location] = [string]
    
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hashVal = self.calculate_hash_value(string)
        if self.table[hashVal] != None:
            return hashVal
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hashVal = (ord(string[0])*100) + ord(string[1])
        return hashVal
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
