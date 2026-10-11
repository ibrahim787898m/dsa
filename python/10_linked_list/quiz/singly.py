class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None

def insert_front(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head
    while current is not None:
        old = current
        current = current.next

    old.next = new_node
    return head

def insert_end_fast(head, tail, data):
    new_node = Node(data)

    if head is None:
        return new_node, new_node

    tail.next = new_node
    tail = new_node

    return head, tail

def insert_front_fast(head, tail, data):
    new_node = Node(data)
    new_node.next = head

    if head is None:
        tail = new_node

    head = new_node

    return head, tail

def search(head, target):
    current = head
    while current is not None:
        if current.data == target:
            return True
        current = current.next

    return False

def delete_front(head):
    if head is None:
        return None

    return head.next

def delete_value(head, target):
    if head is None:
        return None

    if head.data == target:
        return head.next

    current = head
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            return head

        current = current.next

    return head

def delete_value_using_dummy(head, target):
    dummy = Node(0)
    dummy.next = head

    current = dummy
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            break

        current = current.next

    return dummy.next

def delete_last(head):
    dummy = Node(0)
    dummy.next = head

    if head is None:
        return None

    current = dummy
    while current.next is not None:
        old = current
        current = current.next 

    old.next = current.next

    return dummy.next

def delete_all(head, target):
    dummy = Node(0)
    dummy.next = head

    current = dummy
    while current.next is not None:
        old = current
        if current.next.data == target:
            current.next = current.next.next
            current = old
        else:
            current = current.next

    return dummy.next


def index_of(head, target):
    index = 0
    current = head
    while current is not None:
        if current.data == target:
            return index
        index += 1
        current = current.next

    return -1

def delete_value_fast(head, tail, target):
    dummy = Node(0)
    dummy.next = head

    current = dummy
    while current.next is not None:
        if current.next.data == target:
            if current.next is tail:
                if current is dummy:
                    tail = None
                else:
                    tail = current
            current.next = current.next.next
            return dummy.next, tail
        
        current = current.next
    return dummy.next, tail
        


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def reverse(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

#head = None
head = Node(1)
#head.next = Node(2)
#head.next.next = Node(3)

print_list(head)
head = reverse(head)
print_list(head)

#
#head, tail = None, None
#for value in [3, 7, 3]:
#    head, tail = insert_end_fast(head, tail, value)
#
#head, tail = delete_value_fast(head, tail, 3)
#
#print_list(head)
#print("tail:", tail.data if tail else None)

#
#head = Node(3)
#head.next = Node(7)
#head.next.next = Node(1)
#head = index_of(head, 1)
#print(head)

#
#head = Node(1)
#head.next = Node(3)
#head.next.next = Node(3)
#head.next.next.next = Node(5)
#head = delete_all(head, 3)
#print_list(head)
    

#
#head = None
#head = delete_last(head)
#print_list(head)

#
#head = None
#head = insert_end(head, 3)
#head = insert_front(head, 1)
#head = insert_end(head, 5)
#print_list(head)
#
#
#head, tail = None, None
#head, tail = insert_front_fast(head, tail, 8)
#head, tail = insert_end_fast(head, tail, 9)
#head, tail = insert_front_fast(head, tail, 7)
#print_list(head)
#print("tail:", tail.data) 
