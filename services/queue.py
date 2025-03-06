queue = []

class Queue:
    def __init__(self):
        self.items = [] 

    def enqueue(self, item):
        # if len(self.items) >= 10:
        #     self.items.pop(-1) 
        self.items.append(item)

    def dequeue(self, item):
        self.items.pop(int(item))  

    def clear(self):
        self.items.clear()        

    def length(self):
        return len(self.items)

    def __str__(self):
        return self.items
    
    def next(self):
        return self.items[:10]
    
    def nextelement(self):
        self.items.pop(0)

print(queue)

queue = Queue()