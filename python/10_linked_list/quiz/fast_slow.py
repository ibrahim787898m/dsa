class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None

def print_list_forward(head):
    seen = set()
    current = head
    while current is not None:
        if current in seen:
            print(f"{current.data} (cycle detected)")
            break
        print(current.data, end=" -> ")
        seen.add(current)
        current = current.next

    if current is None:
        print("None")


def middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle_set(head):
    seen = set()
    current = head
    while current is not None:
        if current in seen:
            return True
        current = current.next
    return False

def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# def  kth_from_end(head, k):
#     head = reverse(head)
#     i = 0
#     current = head
#     while current is not None:
#         i += 1
#         if i == k:
#             return current.data
#         else:
#             current = current.next
#     return None

def kth_from_end(head, k):
    slow = head
    fast = head
    i = 0
    while fast is not None:
        i += 1
        if i > k:
            slow = slow.next
        fast = fast.next
    if i < k:
        return None
    return slow.data

def is_palindrome_fast(head):
    # find middle wihth fast and slow pointer
    # reverse the second half in place
    # compare the first half and the reversed second half

    # empty list
    if head is None:
        return True

    # finding the middle point
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half
    prev = None
    current = slow
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # compare the first half and the reversed second half
    first_half = head
    second_half = prev

    while first_half is not None and second_half is not None:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

# empty list test case
head = None
print(is_palindrome_fast(head))

# one Node 
head = Node(1)
print(is_palindrome_fast(head))

# 1 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
print(is_palindrome_fast(head))

# 1 -> 2 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
print(is_palindrome_fast(head))
print_list_forward(head)

# 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(is_palindrome_fast(head))
print_list_forward(head)

# 1 -> 2
# head = Node(1)
# head.next = Node(2)
# print(is_palindrome_fast(head))

# print list after the call
# print_list_forward(head)


# empty list
# head = None
# print_list_forward(head)
# res = kth_from_end(head, 2)
# print(res)


# 10 -> 20 -> 30 -> 40 -> 50
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# print_list_forward(head)
# res = kth_from_end(head, 7)
# print(res)
# print_list_forward(head)

# empty linked list
# head = None
# res = has_cycle(head)
# print(res)

# one node, no loop
# head = Node(1)
# res = has_cycle(head)
# print(res)

# one node, pointing to itself
# head = Node(1)
# head.next = head
# res = has_cycle(head)
# print(res)

# 1 -> 2 -> 3 -> 4 (no cycle)
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# print_list_forward(head)
# res = has_cycle(head)
# print(res)

# 1 -> 2 -> 3 -> 4, with [4] pointing back to [1]
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = head
# print_list_forward(head)
# res = has_cycle(head)
# print(res)

# 1 -> 2 -> 3 -> 4 -> 5, with [5] pointing back to [3]
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# head.next.next.next.next.next = head.next.next
# print_list_forward(head)
# res = has_cycle(head)
# print(res)


# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# print_list_forward(head)
# head = reverse(head)
# print_list_forward(head)

# print(middle(head).data)