### SRC- Great, but would have liked to see more testing at the end.
queue = []
size = len(queue)
maxSize = 5

def isEmpty(q):
    return len(q) == 0
#endprocedure - this is a function not a procedure

def isFull(q):
    return len(q) == maxSize
#endprocedure

def enQueue(q, item):
    if not isFull(q):
        q.append(item)
    else:
        print("Full")
    #endif
#endprocedure

def deQueue(q):
    if not isEmpty(q):
        return q.pop()
    else:
        print("Empty")
    #endif
#endprocedure - this is a function not a procedure

enQueue(queue, "socks")
print(queue)
deQueue(queue)
print(queue)
print(isFull(queue))
print(isEmpty(queue))

