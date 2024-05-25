stack = []

def push(stack , item):
    if type(item)==int:
        stack.append(item)
    else:
        for i in item:
            stack.append(i)

def pop(stack):
    if not is_empty(stack): # type: ignore
        return stack.pop()
    return None 

def peek(stack):
    if not is_empty(stack):  # type: ignore
        return stack[-1]
    
def is_empty(stack):
    return len(stack) == 0 

def size(stack):
    return len(stack)
lst = [2,3,4,5]
push(stack ,lst)
push(stack , 5)
push(stack , 2)
pop(stack)
print(is_empty(stack))
print(size(stack))
print(stack)
