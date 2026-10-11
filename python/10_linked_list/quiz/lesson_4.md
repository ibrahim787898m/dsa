# Linked List — Quiz: Lesson 4

The same workflow as before: trace or code, run it, send it with the output, and tell me when you're done.

New this lesson, based on what happened in Lesson 3: each code question lists its edge cases. If anything is still unclear, ask before you code.

## Q1 (trace)

**Start with 1 <-> 2 <-> 4. Insert 3 after [2] using the four lines from section 3, but skip line 3 (`node.next.prev = new_node`).**

- Draw the result.
- What does a forward traversal from head print?
- What does a backward traversal from tail print?
- Explain in one sentence why they disagree.

```
1 <-> 2 <-> 4
node = 2
new_node = 3
```

```python
new_node.prev = node
new_node.next = node.next
node.next.prev = new_node #skip this line
node.next = new_node
```

1st line: new_node.prev = node is gonna point new node 3 to node 2 like 1 <-> 2 <- 3 look 2 is not pointing at 3, it is pointing at 4 still but 4 lost its point to 2 because new node is now pointing at 2. thats important.

2nd line: new_node.next = node.next = 2.next, so as 2 is still pointing at 4 2.next node is 4 so now after this line new node is gonna point to 4 and 2 will lost the pointer with 4 as new node is pointing so it will look like 1 <-> 2 <- 3 -> 4. so we made pointer from new node to both prev 2 node and next next 4 node but node 2 and 4 still not pointing at 3 because 4 is still pointing at 2 and 2 is still pointing at 4. and we will use this to make pointer between new node and both node.

3rd line: as we skip line 3 node_next is 4 and 4.prev is not gonna make pointer with new node

4th line: node.next which is node 2 is gonna make pointer with new node 3 and it will look like 1 <-> 2 <-> 3 -> 4 (pointing at node 2) but see 4 is still pointing at node 2 because we skipped line 3 and did not make pointer from 4 to new node 3.

```
1 <-> 2 <-> 3 -> 4 (pointing at node 2)
```

now do the forward traversal from head:

```python
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
```

- 1st run print: 1
- 2nd run print: 2
- 3rd run print: 3
- 4th run print: 4
- 5th run current is None loop stops print: None

so result: 1 -> 2 -> 3 -> 4 -> None Looks normal

now do the backward traversal from tail: where we will see the problem

```python
current = tail
while current is not None:
    print(current.data, end=" <- ")
    current = current.prev
print("None")
```

- 1st run print: 4 looks good.
- 2nd run print: 2 wait a minute it should print 3 yeah here is the bug. 4.prev is not 3 it is 2 because we skip the line 3 and 4 is still pointing at 2.
- 3rd run print: 1
- 4th run current is None loop stops print: None

so result: None <- 1 <- 2 <- 4

## Q2 (code)

**Write `check(head, tail)`, which returns True if the doubly linked list is consistent and False if not. Consistent means all of these hold:**

- If the list is empty, both head and tail are None.
- head.prev is None and tail.next is None.
- For every node with a next: node.next.prev is node.
- Walking forward from head ends at tail.

**Edge cases to test: an empty list, one node, a correct 3-node list, and the broken list from Q1 (it should return False).**

### First attempt

```python
def check(head, tail):
    bool = False

    if head is None and tail is None:
        return True

    current = head

    if current is head and current is tail:
        if current.prev is None and current.next is None:
            return True

    while current is not None:
        if current is head and current.prev != None:
            return False
        if current is tail and current.next != None:
            return False
        if current is tail:
            return True
        elif current is not tail and current.next is None:
            break
        if current.next.prev is current:
            current = current.next
        elif current.next.prev is not current:
            return False
        bool = True

    if current is not tail:
        bool = False

    return bool


#empty list test
#head, tail = None, None

#single node test
s = DNode(5)

#a correct 3 node list
a, b, c = DNode(1), DNode(2), DNode(3)
a.next = b
b.prev = a
b.next = c
c.prev = b

#a broken list
m, n, l = DNode(1), DNode(2), DNode(3)
m.next = n
n.prev = m
n.next = l
l.prev = m


head, tail = m, l

res = check(head, tail)

#print(res)


# case A: head is real, but tail = None
i, j, k = DNode(1), DNode(2), DNode(3)
i.next = j; j.prev = i
j.next = k; k.prev = j

print(check(i, None))          # expected: False


# case B: tail is a node that isn't in the list
x = DNode(9)                   # a separate, unconnected node
print(check(i, x))             # expected: False
```

### Cleanup version

```python
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
```

## Q3 (code)

**Write `insert_after(head, tail, node, data)`, which inserts a new node after node and returns (head, tail). You can assume node is in the list and isn't None. Edge cases to test:**

- node is in the middle
- node is the tail, so tail must change
- node is the only node

**Run `check()` after every test.**

### First attempt

```python
def insert_after(head, tail, node, data):
    new_node = DNode(data)

    if head is None:
        return new_node, new_node

    if node is tail:
        node.next = new_node
        new_node.prev = node
        tail = new_node
    else:
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node

    return head, tail

#single node
s = DNode(5)

#node is tail
a, b, c = DNode(1), DNode(2), DNode(3)
a.next = b
b.prev = a
b.next = c
c.prev = b


head, tail = a, c

head, tail = insert_after(head, tail, b, 4)

print_forward(head)
print_backward(tail)

print(check(head, tail))
```

### Cleanup version

```python
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
```

## Q4 (trace and find the bugs)

**Someone wrote a shorter `delete_node`:**

```python
def delete_node(head, tail, node):
    node.prev.next = node.next
    node.next.prev = node.prev
    return head, tail
```

**For each case (deleting a middle node, the head, the tail, and the only node), say whether it works, crashes (and on which line), or runs but leaves head/tail wrong.**

```
1 <-> 2 <-> 3
```

### Case 1: middle node 2

1st line: node.prev is 1 and node is 2. 1.next = 2.next -> which is gonna go over the node and connect pointer from 1 to 3. 1 -> 3 alongside node is pointing at 1 and 3 and 3 is also pointing at 2

2nd line: node.next is 3 and node is 2. 3.prev = 2.prev -> which is gonna connect pointer from 3 to 1. 1 <-> 3 and now none of these pointing at 2 anymore so 2 got removed.

3rd line: will return head 1 and tail 3 as head and tail did not change.

result: works for middle node.

### Case 2: head [1]

1st line: node is head and it is 1 so if we do node.prev which is nothing and the code is gonna crush immediately.

### Case 3: tail [3]

1st line: node is tail and it is 3 so if we do node.prev which is 2 so 2.next = 3.next which is none so now 2 is pointing at None 1 <-> 2 -> None.

2nd line: now 2 is pointing at None so node.next is nothing because node is not pointing at none and the code is gonna crush.

### Case 4: one node list [5]

1st line: node is 5 and the node.prev is nothing and the code is gonna crush is the first line.

## Q5 (circular, code)

**Use a circular singly linked list with only tail (no head variable). Write:**

- `insert_end_circ(tail, data)` returns the new tail
- `print_circ(tail)` prints all values once, starting from the head

**Edge cases to test: inserting into an empty list (tail is None), building 1 -> 2 -> 3, and printing an empty list. Then answer in one or two sentences: why is tail alone enough, while head alone wouldn't be?**

```
1 -> 2 (tail) -> 1

new data = 3

1 -> 2 -> 3 (tail) -> 1

print
1 -> 2 -> 3
back to start
```

### Part A

```python
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
```

### Part B

only head is not possible because to insert end we need the last node and which is tail. if only tail it works and also when we do tail.next we get the head actually but we cant do head.prev because it is a circular list, no prev pointer.
