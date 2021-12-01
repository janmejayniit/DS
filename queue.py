class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def enqeue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items

q = Queue()
q.size()
q.enqeue('hello')
q.enqeue('dog')
q.enqeue(3)
print(q.show())
q.dequeue()
print(q.size())
print(q.show())