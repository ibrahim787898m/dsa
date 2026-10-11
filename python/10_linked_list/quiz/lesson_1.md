# Linked List — Quiz: Lesson 1

Answer in your own words. No running code for these. Trace them by hand.

## Q1

**Why is accessing the 5th element O(1) in an array but O(n) in a linked list? Explain it in terms of memory.**

when we access the 5th element of an array, computer can jumps directly to 5th element because computer knows the start of the array and he will calculate with start + 5 * size and get the 5th element and this line of math is only O(1) times. and when accessing from a linked list computer has to walk through the list to find out the 5th element because computer only knows the head and the nodes and it will use current = head -> current = current.next to walk through the linked list to find the 5th element.

## Q2

**What does this print?**

```python
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head = head.next
current = head
while current:
    print(current.data)
    current = current.next
```

this print value 20 and 30 and skip 10. because check the 4th and 5th line when we write head = head.next (which is Node(20)) and current = head = head.next = Node(20) so first it will print value of current Node which is 20 and make the current = current.next and as current is now 20 so it is pointing at Node(30) so current.next is Node(30) so next it print value 30 and then again current = current.next which is None and end the loop.

**What happened to the node holding 10?**

## Q3

**Write a function `length(head)` that returns how many nodes are in the list. It should return 0 for an empty list (head is None).**

```python
def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

print(length(head))   # 3
print(length(None))
```

## Q4

**You need a data structure where you'll constantly add items to the front and almost never look items up by position. Array or linked list? Why?**

linkd list because to add items in the front we just need the head for linked list and it can add items in the front changing the head only dont even need to move the entire list so it is O(1) fast. if array we need to move the elements forward one by one to fit the new one at the beggining so it cost O(n).

## Q5 (think harder)

**This loop has a bug. What is it, and what happens when you run it?**

```python
current = head
while current.next is not None:
    print(current.data)
    current = current.next
```

there are 2 bugs. one is in the condition line while current.next is not None. look carefully when current is 7 current.next is None so before printing 7 we are ending the loop by this condition. we should do while current is not None to print all 3 values. and another bug is when we have an empty linked list we are not printing anything we should print None at the end if no element.
