""" 
Design a very simple array data structure with core functionality
"""
class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        deleted_item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
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

