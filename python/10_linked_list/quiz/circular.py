class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None

def print_circular(head):
    if head is None:
        print("(empty)")
        return

    current = head
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current is head:
            break
    print("(back to start)")


def insert_end_circ(tail, data):
    new_node = Node(data)

    if tail is None:
        tail = new_node
        new_node.next = new_node

    else:
        new_node.next = tail.next
        tail.next = new_node
        tail = new_node

    return tail

def print_circ(tail):
    if tail is None:
        print("(empty)")
        return

    current = tail
    while True:
        print(current.next.data, end=" -> ")
        current = current.next
        if current is tail:
            break

    print("(back to start)")


tail = None

tail = insert_end_circ(tail, 1)
tail = insert_end_circ(tail, 2)
tail = insert_end_circ(tail, 3)

print_circ(tail)

print(tail.data)

print(tail.next.data)

print_circ(None)



# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = head

# n = Node(5)
# n.next = n

# print_circular(head)
# print_circular(None)

# print_circular(n)


