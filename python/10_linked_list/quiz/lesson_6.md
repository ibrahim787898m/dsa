# Linked List — Quiz: Lesson 6

The same workflow: trace or code → run it → send all test output → check every part of the question → tell me when you're done.

## Q1 (trace)

**Use the same table as section 1 (slow, fast, continue?):**

**Trace `middle()` on 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.**

**Trace it on 1 -> 2 -> 3 -> 4 -> 5 -> 6.**

**Even-length lists have two middles. Which one does `middle()` return: the first middle or the second?**

```python
def middle(head):
	slow = head
	fast = head
	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
	return slow
```

**1st trace:** 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

```text
1st line: slow = head = 1
2nd line: fast = head = 1
3rd line: loop runs: fast is 1 not None and fast.next is 2 not None:
	4th line: slow = 1.next = 2
	5th line: fast = 1.next.next = 3
3rd line: loop runs: fast is 3 not None and fast.next is 4 not None:
	4th line: slow = 2.next = 3
	5th line: fast = 3.next.next = 5
3rd line: loop runs: fast is 5 not None and fast.next is 6 not None:
	4th line: slow = 3.next = 4
	5th line: fast = 5.next.next = 7
3rd line: loops stops: fast is 7 not None but fast.next is None
6th line: return slow which is 4
```

**2nd trace:** 1 -> 2 -> 3 -> 4 -> 5 -> 6

```text
1st line: slow = head = 1
2nd line: fast = head = 1
3rd line: loop runs: fast is 1 not None and fast.next is 2 not None:
	4th line: slow = 1.next = 2
	5th line: fast = 1.next.next = 3
3rd line: loop runs: fast is 3 not None and fast.next is 4 not None:
	4th line: slow = 2.next = 3
	5th line: fast = 3.next.next = 5
3rd line: loop runs: fast = 5 not None and fast.next is 6 not None:
	4th line: slow = 3.next = 4
	5th line: fast = 5.next.next = None
3rd line: loop stops: fast is None(no need to check second condition)
6th line: return slow which is 4
```

- so for the even list the second middle one is gonna return. because see when the slow moves forward 3 times fast also move 3 times by in 2 step 3 * 2 = 6 which is None and stop loop and at 3rd loop the slow is at 4th index of the list. so if the even list has 8 values the loop will run 4 times and fast will be 4 * 2 = 8 which is None and stop and return the 5th index value. 

## Q2 (trace and find the bug)

**Someone swapped the loop condition:**

```python
while fast.next is not None and fast is not None:
```

**Trace it on 1 -> 2 -> 3 and on 1 -> 2 -> 3 -> 4. Which one works and which one crashes, on which check, and why? What happens on an empty list? Then explain in one sentence why the order of the two checks matters.**

```python
def middle(head):
	slow = head
	fast = head
	while fast.next is not None and fast is not None:
		slow = slow.next
		fast = fast.next.next
	return slow
```

**1st trace:** 1 -> 2 -> 3

```text
1st line: slow = head = 1
2nd line: fast = head = 1
3rd line: loop 1: fast.next = 2, fast = 1 -> run
	4th line: slow = 1.next = 2
	5th line: fast = 1.next.next = 3
3rd line: loop 2: fast.next = None -> stop (first condition false so stop here without checking the second one)
6th line: return slow which is 2
```

**2nd trace:** 1 -> 2 -> 3 -> 4

```text
1st line: slow = head = 1
2nd line: fast = head = 1
3rd line: loop 1: fast.next = 2, fast = 1 -> run
	4th line: slow = 1.next = 2
	5th line: fast = 1.next.next = 3
3rd line: loop 2: fast.next = 4, fast = 3 -> run
	4th line: slow = 2.next = 3
	5th line: fast = 3.next.next = None
3rd line: loop 3: fast.next = None.next = which is nothing and we will get Nanotype error and it will crush
```

- why the 2nd one crush, 1st one did not although we did use the swapped condition for both case? look when we are working on a even linked list after some loop the fast moves to None and when we check the fast.next before fast it crush because fast.next is nothing for this case but odd list we always land to the last value which one is just before none and for this case fast.next is None which is where the loop stop instead of crushing and return the slow. 

now lets check for an empty list

**3rd trace:** head = None

```text
1st line: slow = head = None
2nd line: fast = head = None
3rd line: loop 1: fast.next = None.next = again it is nothing and crush and give us Nanotype error. if we check fast first it would match the condition and stop the loop and return the slow as None.
```

- so to avoid the None.next = Nothing, Nanotype error we need to check the fast first and then first.next.

## Q3 (code)

**Write has_cycle(head) in fast_slow.py using fast and slow pointers (no set). Build each test list by hand. Edge cases to test:**

| list | expected |
|---|---|
| empty | False |
| one node, no loop | False |
| one node pointing to itself | True |
| 1 -> 2 -> 3 -> 4 (no cycle) | False |
| 1 -> 2 -> 3 -> 4, with [4] pointing back to [1] | True |
| 1 -> 2 -> 3 -> 4 -> 5, with [5] pointing back to [3] | True |

**Don't call print_list on a cyclic list. You already know why.**

```python
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

def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

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
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next
print_list_forward(head)
res = has_cycle(head)
print(res)
```

## Q4 (code)

**Write kth_from_end(head, k), which returns the value of the k-th node from the end (k = 1 means the last node), in one pass. If k is larger than the list length, return None. Tests on 10 -> 20 -> 30 -> 40 -> 50:**

| k | expected |
|---|---|
| 1 | 50 |
| 2 | 40 |
| 5 | 10 |
| 6 | None |

**Also test an empty list with k = 1, which should give None.**

```python
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

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def  kth_from_end(head, k):
    head = reverse(head)
    i = 0
    current = head
    while current is not None:
        i += 1
        if i == k:
            return current.data
        else:
            current = current.next
    return None

# empty list
head = None
print_list_forward(head)
res = kth_from_end(head, 1)
print(res)

# 10 -> 20 -> 30 -> 40 -> 50
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# print_list_forward(head)
# res = kth_from_end(head, 6)
# print(res)
```

here is all 5 test cases with code. done.

**Fix:** make it only one pass instead of two pass

```python
def kth_from_end(head, k):
    slow = head
    fast = head
    i = 0
    while fast is not None:
        if i < k:
            fast = fast.next
            i += 1
        else:
            slow = slow.next
            fast = fast.next
    return slow

# empty list
head = None
print_list_forward(head)
res = kth_from_end(head, 1)
print(res)

# 10 -> 20 -> 30 -> 40 -> 50
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# print_list_forward(head)
# res = kth_from_end(head, 5)
# print(res.data)
```

with all 5 cases and code. i did not notice the one pass one in the question because in my all previous questions there was not anything like one pass. and after seeing the problem i immediately thought about the reverse func and the prev method. 

**Fix:** wrong output of the edge case where k = 6

```python
def kth_from_end(head, k):
    slow = head
    fast = head
    i = 0
    while fast is not None:
        if i < k:
            fast = fast.next
            i += 1
        else:
            slow = slow.next
            fast = fast.next
    if k - i == 1:
        return None
    return slow.data

# empty list
head = None
print_list_forward(head)
res = kth_from_end(head, 1)
print(res)

# 10 -> 20 -> 30 -> 40 -> 50
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# print_list_forward(head)
# res = kth_from_end(head, 6)
# print(res)
```

now i tested the other edge case and it is None

**Fix:** wrong output of edge cases where k = 7 or 8 and empty list with k = 2

```python
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
```

## Q5 (think harder, code)

**In Lesson 5, your is_palindrome used O(n) space for the copy. Write is_palindrome_fast(head) using O(1) extra space:**

1. **Find the middle with fast/slow.**
2. **Reverse the second half in place, using your reverse from Lesson 5.**
3. **Compare the first half with the reversed second half.**

**Test the same six cases as Lesson 5 Q5. Then answer:**

**Does your function change the original list? Print it after calling the function and show what happened.**

**In one sentence: what's the trade-off between this version and the Lesson 5 version?**

```python
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

# 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(is_palindrome_fast(head))

# 1 -> 2
head = Node(1)
head.next = Node(2)
print(is_palindrome_fast(head))

# print list after the call
print_list_forward(head)
```

- it does change the original list because when we locate the middle node, we reversed the next half of the list and because of it when printing from head when we reach the middle point we cant get the rest half as the rest half already reversed and pointing in different direction.
- first of all in this version we are not making any copy of the list in reverse we are just separating the list in half and reversing another half and comparing both half where we did not use space so space is down to O(1) from O(n). the problem is we needed to run multiple passes, multiple while loop to do each steps.
