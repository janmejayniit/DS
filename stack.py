#Completed implementation of a stack ADT

class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else print('Stack is empty')
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

    def show(self):
        return self.items

s = Stack()

''' Call Stack method to perform stack operations '''
'''
s.push('Tom')
s.push('Kiaol')
s.push('Robert')
s.push('kristy')
print(s.size())
print(s.show())
s.pop()
s.pop()
print(s.size())
print(s.show())
'''