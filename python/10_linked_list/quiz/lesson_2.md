# Linked List — Quiz: Lesson 2

Trace by hand. Draw boxes and arrows, and use a trace table like the one in Q5.

## Q1

**Start with an empty list (head = None). What does the list look like after this?**

```python
head = insert_front(head, 1)
head = insert_end(head, 2)
head = insert_front(head, 3)
head = insert_at(head, 1, 4)
```

3412

## Q2

**Someone wrote `insert_after` with the steps swapped:**

```python
prev_node.next = new_node
new_node.next = prev_node.next
```

**Run it on 5 -> 3 -> 7 with prev_node = [3], inserting 9. Draw the result. What goes wrong, specifically?**

insert 9
prev_node = 3 prev_node.next = 7

when we do prev_node.next = new_node we are trying to connect pointer to new node from 7 but it is not the prev node. for insert_after we need to point the new node 9 to the node which one was just after the prev_node which is 7 so connect point from 9 to 7 node and so we need to write new_node.next = prev_node.next

and then next mistake is new_node.next = prev_node.next. here we need to point to the new node from the prev_node instead we are making point from new node to the node after the prev_node. correct is  prev_node.next = new_node

make sure to point prev node next from new node first then make point from prev node to new node

## Q3

**This caller has a bug. What prints, and why?**

```python
head = Node(3)
insert_front(head, 1)
current = head
while current:
    print(current.data)
    current = current.next
```

first the list was with one element 3 and head is 3
in second line we do add 1 in front so now list has 2 element 1, 3 and head is now 1
3rd line current = head which mean current is now 1
now loop true -> print value 1 -> make current = current.next = 3
loop true -> print value 3 -> make current = current.next = which is None
loop true no break -> print None -> make current = current.next = which is nothing and code breaks. error.

## Q4

**Write `insert_end` using `while current is not None` instead of `while current.next is not None`. Can you make it work? If yes, show how. If not, explain exactly why not.**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_end(head, data):
    new_node = Node(data)

    if haed is None:
        return new_node

    current = head
    while current is not None:
        current = current.next

    current.next = new_node

    return head
```

if we do this at a point current become None and None.next is nothing and we cant add another node here.

so to make it work we need to store the previous current in a old variable and do old.next = new_node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
```

## Q5 (think harder)

**We want O(1) inserts at both ends, so we keep two variables, head and tail. Write `insert_end_fast`.**

```python
def insert_end_fast(head, tail, data):
    new_node = Node(data)

    if head is None:
        head = new_node
        tail = new_node
        return head, tail

    tail.next = new_node
    tail = new_node

    return (head, tail)
```

### Q5 part 2

**Here's `insert_front` again:**

```python
def insert_front(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
```

**Now you're also tracking tail. Start with an empty list (head = None, tail = None) and call `insert_front` to add 8.**

- What are head and tail afterwards?
- Is tail correct?
- What would go wrong if you then called `insert_end_fast(head, tail, 9)`?
- When does `insert_front` need to update tail? Is it always, or only in one case?

Trace it with a drawing, the same way you did Q3 this morning.

start :
```
head = None
tail = None
```

after calling insert_front to add 8:

```
head -> 8 -> None
tail -> None
```

which is not correct because here only one value so head and tail must point at this one value 8 but tail is pointing at None

so tail is not correct.

at this point if we call insert_end_fast(head, tail, 9):
tail is None so tail.next is nothing and we will bet error in tail.next = new_node.

```python
def insert_front(head, data):
    new_node = Node(data)
    new_node.next = head

    if head is None:
        tail = new_node

    head = new_node
```

we just need to point tail to the new node before pointing head to new node

## Q2 (new version)

**Start with 4 -> 8 -> 6. Let a = [4] (the first node) and new_node = Node(5). Someone runs:**

```python
a.next = new_node
new_node.next = a.next
```

**Draw the list after each line. Then: what does a traversal from [4] print? Which node(s) are lost?**

4 -> 8 -> 6, a = [4], new_node = Node(5)

1st line:
a.next = new_node when this line runs 4 points at new node like 4 -> 5
but we forgot to point to the node 8 from the new node so 5 is not pointing at 8 and because of it there are 2 separate chain 4 -> 5 and 8 -> 6 after the first line run.

2nd line:
now a.next is the new node which is 5 not 8 so when we run new_node.next = a.next we are point at new node from new node.

and for that we lost track of node 8

## Q3 (new version)

**Trace this and give the exact output:**

```python
head = Node(2)
head = insert_end(head, 4)
insert_front(head, 9)
head = insert_front(head, 1)

current = head
while current:
    print(current.data)
    current = current.next
```

1st line: head = Node(2) make a new linked list with only 2

2nd line: head = insert_end(head, 4) -> here head is 2 -> so node head will point to node 4 and make 2 -> 4

3rd line: insert_front(head, 9) -> here we did not mention any head. although new node point to 2 but we did not make new node head here so the linked list is like 9 -> 2 (head) -> 4.

4th line: head = insert_front(head, 1) -> that makes new node 1 head and point it to next node 2. so it creates 1 (head) -> 2 -> 4. there is a thing though look at the node 9 it is not pointing at 1 it will still point at node 2.

5th line: current = head = 1

6th line: loop start
- print current.data which is 1
- make current to current.next which is 2
- loop valid
- print 2
- current becomes 4
- loop valid
- print 4
- current become None
- loop not valid
- end loop

so it prints 1 2 4
