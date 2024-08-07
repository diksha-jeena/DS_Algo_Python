queue = []

def is_empty(queue):
    return len(queue) == 0

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if is_empty(queue):
        return "Underflow! The queue is empty."
    return queue.pop(0)

def front(queue):
    if is_empty(queue):
        return "The queue is empty."
    return queue[0]

def rear(queue):
    if is_empty(queue):
        return "The queue is empty."
    return queue[-1]

def size(queue):
    return len(queue)

def display(queue):
    if is_empty(queue):
        print("The queue is empty.")
    else:
        print("Queue elements are:", queue)

q = []
enqueue(q , 10)
enqueue(q , 20)
enqueue(q , 30)
display(q)  
print(dequeue(q))  
display(q)  
print("Front:", front(q))  
print("Rear:", rear(q))    
print("Size:", size(q))    
