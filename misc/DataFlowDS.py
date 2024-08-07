arr = [1 , 2 , 3 , 4]
stack = []
from stack import push , pop , peek , is_empty , size , display
push(stack , arr)
display(stack)
q = []
from queue import enqueue , dequeue , front , rear , size , display
enqueue(q , stack)
display(q)