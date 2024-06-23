class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Underflow! The queue is empty."
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "The queue is empty."
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            return "The queue is empty."
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("Queue elements are:", self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  
print(q.dequeue())  
q.display()  
print("Front:", q.front())  
print("Rear:", q.rear())    
print("Size:", q.size())    
