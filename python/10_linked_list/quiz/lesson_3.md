# Linked List — Quiz: Lesson 3

Rules from now on:

- Trace questions: show a trace table or drawings.
- Code questions: write it in practice.py, run it, and send the code with the output. Include tests for the empty list and a one-node list.

## Q1 (trace)

**Using the dummy-node `delete_value`, trace `delete_value(head, 6)` on 6 -> 2 -> 6 -> 8. What list is returned? Then trace `delete_value(head, 5)` on the same list.**

```python
def delete_value(head, target):
    dummy = Node(0)          # value doesn't matter
    dummy.next = head

    current = dummy
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            break
        current = current.next

    return dummy.next
```

### Part 1

```text
before start:
list 6 -> 2 -> 6 -> 8, target = 6
1st line:
dummy = Node(0) -> create a new node but still does not point it to head
2nd line:
dummy.next = head -> now dummy node point to the head and it looks like dummy -> 0 -> 6 (head) -> 2 -> 6 -> 8
3rd line:
current = dummy = 0
4th line:
loop start until current.next is None
    5th line: current.next.data = 0.next.data = 6 == target | condition match
        6th line: current.next = current.next.next which is 0.next = 0.next.next = 2 so we are skipping 6 and it becomes dummy 0 -> 2 -> 6 -> 8
        7th line: break the loop
    8th line skip
9th line: return dummy.next which is 2 which will return as head. so it will return 2 (head) -> 6 -> 8
```

### Part 2

```text
before start:
list 6 -> 2 -> 6 -> 8, target = 5
1st line:
dummy = Node(0) -> create a new node but still does not point it to head
2nd line:
dummy.next = head -> now dummy node point to the head and it looks like dummy -> 0 -> 6 (head) -> 2 -> 6 -> 8
3rd line:
current = dummy = 0
4th line:
loop start until current.next is None
    5th line: current.next.data = 0.next.data = 6 != target | condition did not match
        6th line and 7th line skip
    8th line: current = current.next = 0.next = 6
4th line:
loop start again because current.next = 2 not None
    5th line: current.next.data = 6.next.data = 2 != target | condition did not match
        6th line and 7th line skip
    8th line: current = current.next = 6.next = 2
loop start again because current.next = 6 not None
    5th line: current.next.data = 2.next.data = 6 != target | condition did not match
        6th line and 7th line skip
    8th line: current = current.next = 2.next = 6
loop start again because current.next = 8 not None
    5th line: current.next.data = 6.next.data = 8 != target | condition did not match
        6th line and 7th line skip
    8th line: current = current.next = 6.next = 8
loop stops here because current is now 8 and current.next = None

9th line: return dummy.next will return the entire list with head pointing at 6. head -> 6 -> 2 -> 6 -> 8
```

## Q2 (code)

**Write `delete_last(head)`, which removes the last node and returns the head. There's no tail variable. Test it on 3 -> 7 -> 1, on a one-node list, and on an empty list.**

```python
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
```

## Q3 (trace and find the bugs)

**Someone tried to delete every node equal to target:**

```python
def delete_all(head, target):
    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
        current = current.next
    return dummy.next
```

**Trace it on 1 -> 3 -> 3 -> 5 with target = 3. Then trace it on 1 -> 3 with target = 3. There are two different bugs. Find both, then fix the function and run it.**

### 1st trace bug

```text
before start: list 1 -> 3 -> 3 -> 5 target = 3
1st line: make a new node 0, still not point to the head 1
2nd line: dummy 0 point at the head 1 now it looks like dummy -> 0 -> 1 (head) -> 3 -> 3 -> 3 -> 5
3rd line: current = dummy = 0
4th line: loop start: 0.next = 1 is not None:
    5th line: 0.next.data = 1 is not target 3
        6th line: skip
    7th line: current = 0.next = 1
4th line: loop again: 1.next = 3a is not None:
    5th line: 1.next.data = 3a is target 3
        6th line: 1.next = 1.next.next = 3b so 1 is gonna point to 3b and skip 3a so it will look like dummy -> 0 -> 1 (head) -> 3b -> 5
    7th line: current = 1.next = 3b after this line as we skip 3a now we get current 3b and current.next is gonna be 5 and we cant skip the 3b
4th line: loop again: 3b.next = 5 is not None:
    5th line: 3b.next.data = 5 is not target 3
        6th line: skip
    7th line: current = 3b.next = 5
4th line: loop stops: 5.next = None
8th line: return dummy.next which is head -> 1 -> 3b -> 5. we could not skip 3b because after skipping 3a current is 3b and current.next is 5 and 3b got ignored.
```

### 2nd trace bug

```text
before start: list 1 -> 3 target = 3
1st line: make a new node 0, still not point to the head 1
2nd line: dummy 0 point at the head 1 now it looks like dummy -> 0 -> 1 (head) -> 3 -> 3 -> 3 -> 5
3rd line: current = dummy = 0
4th line: loop start: 0.next = 1 is not None:
    5th line: 0.next.data = 1 is not target 3
        6th line: skip
    7th line: current = 0.next = 1
4th line: loop again: 1.next = 3 is not None:
    5th line: 1.next.data = 3 is target 3
        6th line: 1.next = 1.next.next = None so 1 is gonna point to None and skip 3 and list will look like dummy -> 0 -> 1 (head) -> None
    7th line: current = 1.next = None
4th line: it break the code because None.next is nothing and crashes
```

so when we skip the 3, current is 1 and current.next is None and in the while loop None.next is nothing and crashes.

### Fix

```python
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
```

## Q4 (code)

**Write `index_of(head, target)`, which returns the index of the first node equal to target, or -1 if it isn't found. Test it on: found at the head, found in the middle, not found, and an empty list.**

```python
def index_of(head, target):
    index = 0
    current = head
    while current is not None:
        if current.data == target:
            return index
        index += 1
        current = current.next

    return -1


head = Node(3)
head.next = Node(7)
head.next.next = Node(1)
head = index_of(head, 1)
print(head)
```

4 different result for 4 different target

## Q5 (think harder, code)

**Bring back tail from Lesson 2. Write `delete_value_fast(head, tail, target)`, which returns (head, tail). In which situations does tail need to change? Test it on deleting the last node, deleting the only node, and deleting a middle node, and print tail after each.**

tail is the last node so deleting middle node wont effect tail but deleting last node will effect tail and deleting only node will effect tail because only node is both head and tail.

so if the list is 3 (head) -> 7 -> 1 (tail)
delete last node 1 -> make 7 tail before deleteing

if only node list head -> 5 <- tail
deleting only node -> head and tail both should point None

### First attempt

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_value_fast(head, tail, target):
    dummy = Node(0)
    dummy.next = head

    current = dummy
    while current.next is not None:
        if current.next.data == target and current.next is tail and current.next is not head:
            current.next = current.next.next
            tail.next = current
            tail = current
            return dummy.next, tail
        elif current.next.data == target and current.next is tail and current.next is head:
            current.next = current.next.next
            tail.next = current.next
            tail = current.next
            head.next = current.next
            head = current.next
            return dummy.next, tail
        elif current.next.data == target:
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


head, tail = None, None
for value in [7, 3, 3]:
    head, tail = insert_end_fast(head, tail, value)

head, tail = delete_value_fast(head, tail, 3)

print_list(head)
print("tail:", tail.data if tail else None)
```

### Clean version

```python
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
```
