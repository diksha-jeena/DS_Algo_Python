def PUSH(stack , value):
    stack.append(value)
    top = len(stack) -1

def POP(stack):
    if(len(stack) == 0):
        ele = "underflow"
    else:
        ele = stack.pop()
        top = len(stack) -1
        if(len(stack) == 0):
            top = None

def PEEK(stack):
    if(len(stack) == 0):
        print("Empty")
    else:
        top = len(stack) -1
        print("Topmost value = " , stack[top])

def DISPLAY(stack):
    if(len(stack) ==0):
        print("Empty")
    else:
        top = len(stack) -1
        for i in range(top , -1 , -1):
            print(stack[i])

#main
stack = []
top = None
while True:
    print("1 : Push")
    print("2 : Pop")
    print("3 : Print the top most element")
    print("4 : Display the elements")
    print("5 : Exit from the stack")
    choice = int(input("Enter your choice"))
    if(choice == 1):
        value = int(input("Enter the element"))
        PUSH(stack,value)
    elif(choice == 2):
        ele = POP(stack)
        if(ele == "underflow"):
            print("Stack is empty")
    elif(choice == 3):
        PEEK(stack)
    elif(choice == 4):
        DISPLAY(stack)
    elif(choice == 5):
        break
    else:
        print("Invalid choice. Please enter a valid option.")
