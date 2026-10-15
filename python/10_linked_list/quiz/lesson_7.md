# Linked List — Quiz: Lesson 7

Same workflow: trace or code → run it → send all test output → check every part of the question → say done. For the LeetCode questions, test locally first, then submit and send a screenshot of the "Accepted" result as well.

**Put the local code in a new file, `merge.py`.**

## Q1 (trace)

**Trace `merge_sorted()` on a = 1 -> 4 -> 5 and b = 2 -> 3 -> 6, in whatever trace style you like. Then answer:**

**What does it return?**

**After the merge, start from the original a head (node 1) and walk it. What do you see, and why?**

**What happens if a is empty? Trace it briefly.**

```python
def merge_sorted(a, b)
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
```

**trace 1:** a = 1 -> 4 -> 5 and b = 2 -> 3 -> 6

```text
1st line: dummy = Node(0) = 0
2nd line: tail = dummy = 0
3rd line: loop 1: a = 1, b = 2 | run
	4th line: 1 <= 2 | matched 
		5th line: 0.next = 1 | 0 -> 1
		6th line: a = 1.next = 4
	7th, 8th, 9th line skipped 
	10th line: 0.next = 1
3rd line: loop 2: a = 4, b = 2 | run
	4th line: 4 <= 2 | not matched
		5th, 6th line skipped
	7th line: b = 2 is smaller 
		8th line: 1.next = 2 | 0 -> 1 -> 2
		9th line: b = 2.next = 3
	10th line: tail = 1.next = 2
3rd line: loop 3: a = 4, b = 3 | run
	4th line: 4 <= 3 | not matched
		5th, 6th line skipped
	7th line: b = 3 is smaller
		8th line: 2.next = 3 | 0 -> 1 -> 2 -> 3
		9th line: b = 3.next = 6
	10th line: tail = 2.next = 3
3rd line: loop 4: a = 4,  b = 6 | run
	4th line: 4 <= 6 | matched
		5th line: 3.next = 4 | 0 -> 1 -> 2 -> 3 -> 4
		6th line: a = 4.next = 5
	7th, 8th, 9th line skipped
	10th line: tail = 3.next = 4
3rd line: loop 5: a = 5, b = 6 | run 
	4th line: 5 <= 6 | matched
		5th line: 4.next = 5 | 0 -> 1 -> 2 -> 3 -> 4 -> 5
		6th line: a = 5.next = None
	7th, 8th, 9th line skipped
	10 line: tail = 4.next = 5
3rd line: loop 6: a = None | stops
11th line: 5.next = b = 6 | cause a is None | 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
12th line: return dummy.next which is 0.next which is 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
```

- it returns 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
- if i walk from Node(1) to the end i can see the values are merged in sorted order because we did check the conditions to find out the smaller one before merging the it. 

**trace 2:** a = None(empty) and b = 2 -> 3 -> 6

```text
1st line: dummy = Node(0) = 0
2nd line: tail = dummy = 0
3rd line: loop 1: a = None, b = 2 | stops | jumps to 11th line
11th line: tail.next = 0.next = b which is 2 -> 3 -> 6 | 0 -> 2 -> 3 -> 6 (connect all the b Nodes at the end of the dummy)
12th line: return dummy.next which is 0.next which is 2 -> 3 -> 6
```

- so it returns the b linked list exactly as it is

## Q2 (code, LeetCode 21: Merge Two Sorted Lists)

**Write `merge_sorted(a, b)` in `merge.py` without looking at the lesson code. Rebuild it from the idea. Tests:**

| a | b | expected |
|---|---|---|
| empty | empty | empty (None) |
| empty | 1 -> 2 | 1 -> 2 |
| 1 -> 2 | empty | 1 -> 2 |
| 1 -> 3 -> 5 | 2 -> 4 -> 6 | 1 -> 2 -> 3 -> 4 -> 5 -> 6 |
| 1 -> 2 -> 2 | 2 -> 3 | 1 -> 2 -> 2 -> 2 -> 3 |
| 1 | 2 -> 3 -> 4 -> 5 | 1 -> 2 -> 3 -> 4 -> 5 |

**Then submit it on LeetCode 21.**

```python
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

# test 1: a and b both empty
print("test 1: a and b both emtpy")
a = None
b = None
print_list_forward(a)
print_list_forward(b)
merged = merge_sorted(a, b)
print_list_forward(merged)

# test 2: a is empty and b = 1 -> 2
print("test 2: a is empty and b = 1 -> 2")
a = None
b = Node(1)
b.next = Node(2)
print_list_forward(a)
print_list_forward(b)
merged = merge_sorted(a, b)
print_list_forward(merged)

# test 3: a = 1 -> 2 and b is empty
print("test 3: a = 1 -> 2 and b is empty")
a = Node(1)
a.next = Node(2)
b = None
print_list_forward(a)
print_list_forward(b)
merged = merge_sorted(a, b)
print_list_forward(merged)

# test 4: a = 1 -> 3 -> 5 and b = 2 -> 4 -> 6
print("test 4: a = 1 -> 3 -> 5 and b = 2 -> 4 -> 6")
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)
b = Node(2)
b.next = Node(4)
b.next.next = Node(6)
print_list_forward(a)
print_list_forward(b)
merged = merge_sorted(a, b)
print_list_forward(merged)

# test 5: a = 1 -> 2 -> 2 and b = 2 -> 3
print("test 5: a = 1 -> 2 -> 2 and b = 2 -> 3")
a = Node(1)
a.next = Node(2)
a.next.next = Node(2)
b = Node(2)
b.next = Node(3)
print_list_forward(a)
print_list_forward(b)
merged = merge_sorted(a, b)
print_list_forward(merged)

# test 6: a = 1 and b = 2 -> 3 -> 4 -> 5
print("test 6: a = 1 and b = 2 -> 3 -> 4 -> 5")
a = Node(1)
b = Node(2)
b.next = Node(3)
b.next.next = Node(4)
b.next.next.next = Node(5)
print_list_forward(a)
print_list_forward(b)
merged = merge_sorted(a, b)
print_list_forward(merged)

```

## Q3 (code, LeetCode 83: Remove Duplicates from Sorted List)

**Write `delete_duplicates(head)`. The list is sorted; remove nodes so that each value appears only once, and return the head. Tests:**

| input | expected |
|---|---|
| empty | empty |
| 1 | 1 |
| 1 -> 1 -> 2 | 1 -> 2 |
| 1 -> 1 -> 1 | 1 |
| 1 -> 1 -> 2 -> 3 -> 3 | 1 -> 2 -> 3 |
| 1 -> 2 -> 3 | 1 -> 2 -> 3 (unchanged) |

**Then submit it on LeetCode 83.**

```python
def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

print("test 1: empty list")
head = None
print_list_forward(head)
head = delete_duplicates(head)
print_list_forward(head)

print("test 2: one node")
head = Node(1)
print_list_forward(head)
head = delete_duplicates(head)
print_list_forward(head)

print("test 3: 1 -> 1 -> 2")
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
print_list_forward(head)
head = delete_duplicates(head)
print_list_forward(head)

print("test 5: 1 -> 1 -> 1")
head = Node(1)
head.next = Node(1)
head.next.next = Node(1)
print_list_forward(head)
head = delete_duplicates(head)
print_list_forward(head)

print("test 6: 1 -> 2 -> 2 -> 3 -> 3")
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)
print_list_forward(head)
head = delete_duplicates(head)
print_list_forward(head)

print("test 5: 1 -> 2 -> 3")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print_list_forward(head)
head = delete_duplicates(head)
print_list_forward(head)
```

## Q4 (code, LeetCode 19: Remove Nth Node From End of List)

**Write `remove_nth_from_end(head, n)` in one pass, and return the new head. (LeetCode guarantees 1 ≤ n ≤ length.) Hint: you need to stop one node before the node to delete. Think about which lesson's tool handles "what if the node to delete is the head?" Tests:**

| input | n | expected |
|---|---|---|
| 1 -> 2 -> 3 -> 4 -> 5 | 2 | 1 -> 2 -> 3 -> 5 |
| 1 | 1 | empty |
| 1 -> 2 | 1 | 1 |
| 1 -> 2 | 2 | 2 |

**Then submit it on LeetCode 19.**

```python
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
        

print("test 1: 1 -> 2 -> 3 -> 4 -> 5, n = 2")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_list_forward(head)
head = remove_nth_from_end(head, 2)
print_list_forward(head)

print("test 2: 1, n = 1")
head = Node(1)
print_list_forward(head)
head = remove_nth_from_end(head, 1)
print_list_forward(head)

print("test 3: 1 -> 2, n = 1")
head = Node(1)
head.next = Node(2)
print_list_forward(head)
head = remove_nth_from_end(head, 1)
print_list_forward(head)

print("test 4: 1 -> 2, n = 2")
head = Node(1)
head.next = Node(2)
print_list_forward(head)
head = remove_nth_from_end(head, 2)
print_list_forward(head)
```

## Q5 (think harder, LeetCode 143: Reorder List)

**Reorder a list in place from L0 → L1 → … → Ln to L0 → Ln → L1 → Ln-1 → L2 → …. Return nothing; just change the links. Tests:**

| input | expected |
|---|---|
| 1 | 1 |
| 1 -> 2 | 1 -> 2 |
| 1 -> 2 -> 3 -> 4 | 1 -> 4 -> 2 -> 3 |
| 1 -> 2 -> 3 -> 4 -> 5 | 1 -> 5 -> 2 -> 4 -> 3 |

**Before you code, write down which pieces from the cheat sheet you'll use, in what order, and why. That plan is part of the answer. Then code it, test it, and submit on LeetCode 143.**

```python
def reorderList(head):
    if not head or not head.next:
        return

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    current = slow
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next is not None:
        old = current
        current = current.next
    old.next = current.next

    a = head
    b = prev
    dummy = Node(0)
    tail = dummy

    while a is not None and b is not None:
        tail.next = a
        a = a.next
        tail = tail.next

        tail.next = b
        b = b.next
        tail = tail.next

    tail.next = a if a is not None else b

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

```

**Fix:** Inconsistent return, 4th pass, and the special case bug reason

```python
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
```

- when it is one node [1] at a point the 2 list a and b are both same like 1 -> None and 1 -> None and when we merge these 2 same list it create cycle so to avoid this we did check at the beginning if the list is empty or single node list
