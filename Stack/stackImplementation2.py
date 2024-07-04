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
    while(stack.peek() == None):
        return stack

lst = [5 , 6 , 7 ,8]
push(stack , lst)
push(stack , 5)
push(stack , 2)
push(stack , 0)
pop(stack)
print(is_empty(stack))
print(size(stack))
print(stack)
