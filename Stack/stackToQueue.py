stack = []

def push(stack , item):
    if type(item)==int:
        stack.append(item)
    else:
        for i in item:
            stack.append(i)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    return None 

def peek(stack):
    if not is_empty(stack):  
        return stack[-1]
    
def is_empty(stack):
    return len(stack) == 0 

def size(stack):
    return len(stack)

def display(stack):
    while(peek(stack) == None):
        return stack

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

# stack = Stack()
queue = Queue()

push(stack , 2)
push(stack , 4)
push(stack , 6)
push(stack , 1)
display(stack)

while (not is_empty(stack)):
    item = pop(stack)
    queue.enqueue(item)

queue.display()