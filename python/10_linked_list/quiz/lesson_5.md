# Linked List — Quiz: Lesson 5

Workflow: trace or code → run it → send it with the output → check every part of the question → tell me when you're done.

## Q1 (trace)

**Trace `reverse()` on 5 -> 8, a two-node list. Use the same table as section 4 (next_node, what got flipped, prev, current, and the picture after each pass). What does it return?**

```python
def reverse(head):
	prev = None
	current = head

	while current is not None:
		next_node = current.next
		current.next = prev
		prev = current
		current = next_node
	return prev
```

```
5 -> 8
```

1st line: prev = None
2nd line: current = head 5
3rd line loop run: current is 5 is not None
	4th line: next_node = 5.next which is gonna be 8 -> None. keep the next node copy. remember 5 is still pointing at 8 here.
	5th line: 5.next = None is gonna make pointer from 5 to None and remove pointer that was connecting to 8. so now: None <- 5 and 8 -> None.
	6th line: prev = 5
	7th line: current = next_node = current.next = 8
3rd line loop run: current is 8 not None
	4th line: next_node = 8.next which is gonna be None. keep the last node copy. same here 8 is still pointing at None.
	5th line: 8.next = prev = 5. which is gonna make pointer from 8 to 5 and remove pointer that was connecting to None. so now: None <- 5 <- 8 None(alone here)
	6th line: prev = 8
	7th line: current = next_node = current.next = None(the copied one)
3rd line loop stops: current is None
8th line: return prev. where prev is 8 which is new head so it will return the reverse version from 8 -> 5 -> None

## Q2 (trace and find the bug)

**Someone left out `next_node`:**

```python
def reverse_bad(head):
    prev = None
    current = head
    while current is not None:
        current.next = prev
        prev = current
        current = current.next
    return prev
```

**Trace it on 1 -> 2 -> 3 -> 4.**

**How many passes does the loop run?**

**What list does it return?**

**Which nodes are lost?**

**In one sentence: what's the bug, in terms of the save-before-you-move rule?**

1st line: prev = None
2nd line: current = head = 1
3rd line: loop runs: current is 1 not None
	4th line: 1.next = prev = None which is gonna make pointer to None and remove pointer that was connecting to next node 2. so now it will look like None <- 1	2 -> 3 -> 4. look now there is no connection between these 2 node and as we cant reach 2 we cant reach entire these list. lets check what happens next
	5th line: prev = current = 1
	6th line: current = current.next = 1.next which is None. see here we needed to reach the next_node that we copy. but we did not and lost it.
3rd line: loop stops: current is None
7th line: return prev. where prev is 1 and it is now head and it is pointing at None and we will get this list 1 -> None and we wont have the rest cause we lost them and could not reverse them also.

1. only one loop run and stops at next one cause the current becomes None because we lost he next node and cant reach it.
2. return list: 1 -> None
3. lost nodes: 2 -> 3 -> 4 -> None
4. the bug is that we did not make the copy or you can say we did not store the next nodes and we lost them.

## Q3 (code)

**Write `reverse(head)` in `singly.py`, without looking at the lesson code. Rebuild it from the idea of the three pointers. Test it on: empty, one node, two nodes, and 1 -> 2 -> 3 -> 4 -> 5. Print the list before and after each test.**

```python
def reverse_singly(head):
    prev_node = None
    current = head

    while current is not None:
        copied_node = current.next
        current.next = prev_node
        prev_node = current
        current = copied_node

    return prev_node



# empty list
# head = None

# single node
# head = Node(1)

# double node
# head = Node(1)
# head.next = Node(2)

# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# run the func and print the list
head = reverse_singly(head)
print_list(head)
```

## Q4 (code)

**In `doubly.py`, write `reverse_doubly(head, tail)`, which returns `(head, tail)`. Swap prev and next in every node, then swap the ends. Edge cases: empty, one node, three nodes. Run `check()` and both `print_forward` and `print_backward` after each test.
Careful: after you swap a node's pointers, `current.next` no longer points forward. Think about how you move to the next node.**

```
None <- 1 <-> 2 <-> 3 -> None
None <- 3 <-> 2 <-> 1 -> None

None <- 1 <-> 2 <-> 3 <-> 4 -> None
None <- 4 <-> 3 <-> 2 <-> 1 -> None
```

- if empty return head and tail, None and None
- if one node head and tail is that one node so return that one node, head and tail
- if three node, if we swap head and tail and return head and tail it works
- if more than three node swap is not gonna work. we need to do manually step by step

```python
def reverse_doubly(head, tail):
    current = head
    if head is tail:
        return head, tail

    while current is not None:
        next_node = current.next
        prev_node = current.prev
        current.prev = next_node
        current.next = prev_node
        current = next_node

    head, tail = tail, head

    return head, tail    
    

    

# empty list test
# head, tail = None, None
# head, tail = reverse_doubly(head, tail)
# print_forward(head)
# print_backward(tail)
# print(check(head, tail))

# single node test
# s = DNode(5)
# head, tail = s, s
# head, tail = reverse_doubly(head, tail)
# print_forward(head)
# print_backward(tail)
# print(check(head, tail))

# three node
# a, b, c = DNode(1), DNode(2), DNode(3)
# a.next = b
# b.prev = a
# b.next = c
# c.prev = b
# head, tail = a, c
# head, tail = reverse_doubly(head, tail)
# print(head.data)
# print(tail.data)
# print_forward(head)
# print_backward(tail)
# print(check(head, tail))

# more than 3 node
a, b, c, d = DNode(1), DNode(2), DNode(3), DNode(4)
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
head, tail = a, d
head, tail = reverse_doubly(head, tail)
print(head.data)
print(tail.data)
print_forward(head)
print_backward(tail)
print(check(head, tail))
```

when i was doing the rough note or psuedocode i was thinking that for 3 node swap is gonna work but after writing it in code i noticed that the pointer between these numbers does not match up and the list is not accurate and print wrong. cause the head and tail switches but the connection of those head and tail with the middle value did not change i mean the pointer and we lost the middle value and print only 3->None or 1<-None.

and one more thing that i was storing the next nodes but not the prev nodes and when i print the forward i cant get all the values just head with the None but backward was correct cause i store the next nodes and make connection proper for the backward case pointers was accurate but in forward case i did not store the prev nodes and not making pointers properly for this case and made mistake then i fixed it.

## Q5 (think harder, code)

**Write `is_palindrome(head)`, which returns True if the values read the same forwards and backwards.

First write `reversed_copy(head)`, which builds a new reversed list and leaves the original unchanged. Hint: which insert function from Lesson 2 naturally builds a list in reverse order?
Then compare the original and the copy node by node.
Test: empty → True, [7] → True, [1, 2, 2, 1] → True, [1, 2, 3, 2, 1] → True, [1, 2] → False, [1, 2, 3] → False.
Afterwards, print the original list to show it's unchanged.
One-line answer: what's the space complexity of your approach, and why?**

```
1 -> 2 -> 3 -> None

current = head
while current is not None:
current = current.next

new_node = Node(current.data)
new_node.next = head
```

```python
def reversed_copy(head):
    new_head = None
    current = head

    while current is not None:
        new_node = Node(current.data)
        new_node.next = new_head
        new_head = new_node
        current = current.next

    return new_head

def is_palindrome(head):
    new_head = reversed_copy(head)
    current1 = head
    current2 = new_head

    while current1 is not None and current2 is not None:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next

    return True


# node
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

new = reversed_copy(head)
print_list(new)
print_list(head)
print(is_palindrome(head))
```

1. both time and space is O(n) because inside of while loop i am doing it until none so all linked list digit i walkthrough for both of the function. and as we are storing same n number from the linked list space is O(n) too.

i made a mistake while solving the last one. after storing the values from the old linked list i was trying to insert it Infront of the previous head instead of new_head. i was always doing new_node.next = head trying to copy the lesson 2 func and forgot that it was connecting to the old one in this func and getting wrong list each time then realized i need a new_head and add the data from the previous one to this head then make change the new head to next one. may be i was a bit tired that i missed that little point and took so much time.
