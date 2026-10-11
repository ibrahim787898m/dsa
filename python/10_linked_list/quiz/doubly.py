class DNode:
    def __init__(self, data):
        self.data = data
        self.prev: "DNode | None" = None
        self.next: "DNode | None" = None

def print_forward(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def print_backward(tail):
    current = tail
    while current is not None:
        print(current.data, end=" <- ")
        current = current.prev
    print("None")

def insert_front(head, tail, data):
    new_node = DNode(data)
    if head is None:
        return new_node, new_node

    new_node.next = head
    head.prev = new_node
    return new_node, tail

def insert_end(head, tail, data):
    new_node = DNode(data)
    if head is None:
        return new_node, new_node

    new_node.prev = tail
    tail.next = new_node
    return head, new_node

# def insert_middle(head, tail, data):
#     new_node = DNode(data)
#     if head is not None:
#         return new_node, new_node

#     new_node.prev = node
#     new_node.next = node.next
#     node.next.prev = new_node
#     node.next = new_node
#     return head, tail

def delete_node(head, tail, node):
    if node.prev is not None:
        node.prev.next = node.next
    else:
        head = node.next

    if node.next is not None:
        node.next.prev = node.prev
    else:
        tail = node.prev

    return head, tail

def check(head, tail):

    if head is None and tail is None:
        return True

    current = head

    while current is not None:
        if current is head and current.prev is not None:
            return False
        if current is tail and current.next is not None:
            return False
        if current is tail:
            return True
        if current.next is None:
            return False
        if current.next.prev is current:
            current = current.next
        else:
            return False

    return False

def insert_after(head, tail, node, data):
    new_node = DNode(data)

    new_node.prev = node
    new_node.next = node.next

    if node is tail:
        tail = new_node
    else:
        node.next.prev = new_node
        
    node.next = new_node

    return head, tail

# def delete_node(head, tail, node):
#     node.prev.next = node.next
#     node.next.prev = node.prev
#     return head, tail



#single node
s = DNode(5)
#
##node is tail
a, b, c = DNode(1), DNode(2), DNode(3)
a.next = b
b.prev = a
b.next = c
c.prev = b
#
#
head, tail = s, s

head, tail = delete_node(head, tail, s)

# head, tail = insert_after(head, tail, c, 4)

print_forward(head)
print_backward(tail)

print(check(head, tail))



#empty list test
#head, tail = None, None

#single node test
#s = DNode(5)

#a correct 3 node list
#a, b, c = DNode(1), DNode(2), DNode(3)
#a.next = b
#b.prev = a
#b.next = c
#c.prev = b

#a broken list
#m, n, l = DNode(1), DNode(2), DNode(3)
#m.next = n
#n.prev = m
#n.next = l
#l.prev = m


#head, tail = m, l

#res = check(head, tail)

#print(res)


# case A: head is real, but tail = None
#i, j, k = DNode(1), DNode(2), DNode(3)
#i.next = j; j.prev = i
#j.next = k; k.prev = j

#print(check(i, None))          # expected: False


# case B: tail is a node that isn't in the list
#x = DNode(9)                   # a separate, unconnected node
#print(check(i, x))             # expected: False

# print_forward(head)
# print_backward(tail)