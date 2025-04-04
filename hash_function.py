class hashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for characters in key:
            h = h + ord(characters)
        return h % self.MAX
    
    def add_to_hash(self,key,value):
        h = self.get_hash(key)
        found = False
#        self.array[h] = value
        for idx, elements in enumerate(self.array[h]):
            if len(elements) ==2 and elements[0]==key:
                self.array[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.array[h].append((key,value))


    def get_value (self, key):
        h = self.get_hash(key)
#        return self.array[h]
        for elements in self.array[h]:
            if elements[0] ==key:
                return elements[1]
    
    

hashfunction = hashTable()
store_value = hashfunction.add_to_hash('march 6',130)
store_value2 = hashfunction.add_to_hash('march 17',343)
print(store_value)
print(store_value2)
print(hashfunction.array)
get_value = hashfunction.get_value(input("Insert the key: "))
print(get_value)

out = hashfunction.get_hash('march 6')
print(out)
out = hashfunction.get_hash('march 17')
print(out)