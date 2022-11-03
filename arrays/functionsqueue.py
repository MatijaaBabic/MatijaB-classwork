queue = []
size = len(queue)
maxSize = 5

def enQueue(q, item):
    if not is_full(q):
        q.append(item)
    else:
        return; "Full"
    #endif
#endprocedure

def deQueue(q):
    if not is_empty(q):
        return q.pop(0)
    else:
        return; "Empty"
    #endif
#endprocedure

def isEmpty(q):
    if len(q) == 0:
        return; "Empty"
    else:
        return; "Not Empty"
    #endif
#endprocedure

def isFull(q):
    if len(q) == maxSize:
        return; "Full"
    else:
        return; "Not full"
    #endif
#endprocedure

enQueue(queue, "socks")
print(queue)

