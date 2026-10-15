class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None

def print_list_forward(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def merge_sorted(a, b):
    dummy = Node(0)
    tail = dummy
    while a is not None and b is not None:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next

def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def remove_nth_from_end(head, n):
    slow = head
    fast = head
    dummy = Node(0)
    dummy.next = slow
    i = 0
    while fast is not None:
        i += 1
        if i > n:
            dummy = dummy.next
            slow = slow.next
        fast = fast.next
    dummy.next = slow.next
    if i == n:
        return dummy.next
    return head

    # clearer version of the above code
    # slow = head
    # fast = head
    # dummy = Node(0)
    # prev = dummy
    # prev.next = head
    # i = 0
    # while fast is not None:
    #     i += 1
    #     if i > n:
    #         prev = prev.next
    #         slow = slow.next
    #     fast = fast.next
    # prev.next = slow.next
    # return dummy.next

def reorderList(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    current = slow
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # dummy = Node(0)
    # dummy.next = head
    # current = dummy
    # while current.next is not None:
    #     old = current
    #     current = current.next
    # old.next = current.next


    a = head
    b = prev
    # dummy = Node(0)
    # tail = dummy

    while a is not None and b is not None:
        # tail.next = a
        # a = a.next
        # tail = tail.next

        # tail.next = b
        # b = b.next
        # tail = tail.next

        a_next = a.next
        b_next = b.next

        a.next = b
        b.next = a_next

        a = a_next
        b = b_next

    # tail.next = a if a is not None else b


    return head


print("test 1: one node")
head = Node(1)
print_list_forward(head)
head = reorderList(head)
print_list_forward(head)

print("test 2: 1 -> 2")
head = Node(1)
head.next = Node(2)
print_list_forward(head)
head = reorderList(head)
print_list_forward(head)

print("test 3: 1 -> 2 -> 3 -> 4")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
print_list_forward(head)
head = reorderList(head)
print_list_forward(head)

print("test 3: 1 -> 2 -> 3 -> 4 -> 5")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_list_forward(head)
head = reorderList(head)
print_list_forward(head)

        

# print("test 1: 1 -> 2 -> 3 -> 4 -> 5, n = 2")
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# print_list_forward(head)
# head = remove_nth_from_end(head, 2)
# print_list_forward(head)

# print("test 2: 1, n = 1")
# head = Node(1)
# print_list_forward(head)
# head = remove_nth_from_end(head, 1)
# print_list_forward(head)

# print("test 3: 1 -> 2, n = 1")
# head = Node(1)
# head.next = Node(2)
# print_list_forward(head)
# head = remove_nth_from_end(head, 1)
# print_list_forward(head)

# print("test 4: 1 -> 2, n = 2")
# head = Node(1)
# head.next = Node(2)
# print_list_forward(head)
# head = remove_nth_from_end(head, 2)
# print_list_forward(head)


# print("test 1: empty list")
# head = None
# print_list_forward(head)
# head = delete_duplicates(head)
# print_list_forward(head)

# print("test 2: one node")
# head = Node(1)
# print_list_forward(head)
# head = delete_duplicates(head)
# print_list_forward(head)

# print("test 3: 1 -> 1 -> 2")
# head = Node(1)
# head.next = Node(1)
# head.next.next = Node(2)
# print_list_forward(head)
# head = delete_duplicates(head)
# print_list_forward(head)

# print("test 5: 1 -> 1 -> 1")
# head = Node(1)
# head.next = Node(1)
# head.next.next = Node(1)
# print_list_forward(head)
# head = delete_duplicates(head)
# print_list_forward(head)

# print("test 6: 1 -> 2 -> 2 -> 3 -> 3")
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(2)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(3)
# print_list_forward(head)
# head = delete_duplicates(head)
# print_list_forward(head)

# print("test 5: 1 -> 2 -> 3")
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# print_list_forward(head)
# head = delete_duplicates(head)
# print_list_forward(head)

# # test 1: a and b both empty
# print("test 1: a and b both emtpy")
# a = None
# b = None
# print_list_forward(a)
# print_list_forward(b)
# merged = merge_sorted(a, b)
# print_list_forward(merged)

# # test 2: a is empty and b = 1 -> 2
# print("test 2: a is empty and b = 1 -> 2")
# a = None
# b = Node(1)
# b.next = Node(2)
# print_list_forward(a)
# print_list_forward(b)
# merged = merge_sorted(a, b)
# print_list_forward(merged)

# # test 3: a = 1 -> 2 and b is empty
# print("test 3: a = 1 -> 2 and b is empty")
# a = Node(1)
# a.next = Node(2)
# b = None
# print_list_forward(a)
# print_list_forward(b)
# merged = merge_sorted(a, b)
# print_list_forward(merged)

# # test 4: a = 1 -> 3 -> 5 and b = 2 -> 4 -> 6
# print("test 4: a = 1 -> 3 -> 5 and b = 2 -> 4 -> 6")
# a = Node(1)
# a.next = Node(3)
# a.next.next = Node(5)
# b = Node(2)
# b.next = Node(4)
# b.next.next = Node(6)
# print_list_forward(a)
# print_list_forward(b)
# merged = merge_sorted(a, b)
# print_list_forward(merged)

# # test 5: a = 1 -> 2 -> 2 and b = 2 -> 3
# print("test 5: a = 1 -> 2 -> 2 and b = 2 -> 3")
# a = Node(1)
# a.next = Node(2)
# a.next.next = Node(2)
# b = Node(2)
# b.next = Node(3)
# print_list_forward(a)
# print_list_forward(b)
# merged = merge_sorted(a, b)
# print_list_forward(merged)

# # test 6: a = 1 and b = 2 -> 3 -> 4 -> 5
# print("test 6: a = 1 and b = 2 -> 3 -> 4 -> 5")
# a = Node(1)
# b = Node(2)
# b.next = Node(3)
# b.next.next = Node(4)
# b.next.next.next = Node(5)
# print_list_forward(a)
# print_list_forward(b)
# merged = merge_sorted(a, b)
# print_list_forward(merged)

# a =  Node(1)
# a.next = Node(2)
# a.next.next = Node(3)

# b = Node(4)
# b.next = Node(5)

# print_list_forward(a)
# print_list_forward(b)

# merged = merge_sorted(a, b)
# print_list_forward(merged)
