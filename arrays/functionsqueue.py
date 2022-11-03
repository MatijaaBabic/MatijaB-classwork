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

def deQueue(q, item):
    if not is_empty(q):
        return q.pop(0)
    else:
        return; "Empty"
    #endif
#endprocedure

def isEmpty(q)