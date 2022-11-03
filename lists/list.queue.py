queue = []
size = len(queue)
maxSize = 5

def isEmpty(q):
    return len(q) == 0
#endprocedure

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
#endprocedure

enQueue(queue, "socks")
print(queue)
deQueue(queue)
print(queue)
print(isFull(queue))
print(isEmpty(queue))

