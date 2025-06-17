""" 
Basic array data structure
"""
class Array:
    def __init__(self):
        self.length = 0
        self.values = {}

    def get(self, index):
        return self.values[index]

    def push(self, item):
        self.values[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.values[self.length - 1]
        del self.values[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        deleted_item = self.values[index]
        for i in range(index, self.length - 1):
            self.values[i] = self.values[i + 1]
        del self.values[self.length - 1]
        self.length -= 1
        return deleted_item

    def __str__(self):
        return str(self.__dict__)

arr = Array()
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.push(5)
arr.push(6)
arr.delete(2)
print(arr)

