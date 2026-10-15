# Linked List — Concept Notes

Oct 15, 2026 · @Ibrahim Mustafa Opu

## 1. Basics

A linked list is a chain of nodes; each node holds a value and a reference to the next node. The list is only reachable through `head`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None   # forward reference type hint
```

- **head** = first node; **tail** = last node (its `.next` is `None`). An empty list is `head = None`.
- **Arrays vs linked lists:** an array is one contiguous block, so `arr[i]` = start + i × element size, O(1). Linked list nodes are scattered in memory, so reaching position i means walking i links, O(n).
- **Moving `head` loses nodes:** after `head = head.next`, nothing points to the old first node, so it is unreachable (Python frees it). A singly list can never step backwards.
- **Traversal pattern:** never walk with `head` itself; use a copy.

```python
current = head
while current is not None:
    print(current.data)
    current = current.next
```

- **`==` vs `is`:** `a.data == b.data` compares values; `a is b` asks "same node object?". Cycle checks, "have I reached the tail/head" checks and node comparisons use `is`.
- **Assignment copies the reference, not the node:** `x = head` gives a second name for the same node; changing `x.next` changes the list.
- **`AttributeError: 'NoneType' object has no attribute 'next'`** = something you thought was a node is actually `None`. Check the loop condition and the empty/one-node cases.

## 2. Insertion

The rule for every insert: **connect the new node first, then move the old links.** If you overwrite a `.next` before saving what it pointed to, the rest of the list is lost.

```python
def insert_front(head, data):        # O(1)
    new_node = Node(data)
    new_node.next = head              # 1. point new node at old head
    return new_node                   # 2. new node is the new head

def insert_end(head, data):          # O(n) without a tail pointer
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:   # stop ON the last node
        current = current.next
    current.next = new_node
    return head

def insert_after(node, data):        # O(1) when you already hold the node
    new_node = Node(data)
    new_node.next = node.next         # save the rest first
    node.next = new_node
```

- Functions that can change the head must **return the new head**, and the caller must reassign: `head = insert_front(head, 5)`.
- **Tail pointer:** keeping `tail` makes insert-at-end O(1): `tail.next = new_node; tail = new_node`. Every operation must keep `tail` correct, including the empty-list case (head and tail both become the new node).
- **Loop condition decides where you stop:** `while current is not None` ends past the last node; `while current.next is not None` ends on the last node (crashes if `head` is `None`).

## 3. Deletion, search and the dummy node

To delete a node you must stand on the node **before** it and skip over it: `prev.next = prev.next.next`. A singly list can't go back, so you either look one ahead (`current.next.data`) or carry a trailing pointer.

```python
def delete_value(head, value):        # trailing pointer, special-cases the head
    if head is None:
        return None
    if head.data == value:
        return head.next
    prev, current = head, head.next
    while current is not None:
        if current.data == value:
            prev.next = current.next
            return head
        prev, current = current, current.next
    return head

def delete_value_dummy(head, value):  # dummy node: no head special case
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    while prev.next is not None:
        if prev.next.data == value:
            prev.next = prev.next.next
            break
        prev = prev.next
    return dummy.next
```

- **Dummy node:** a fake node in front of the head, so the real head has a "previous" too. `dummy` itself **never moves**; a separate pointer (`prev`, `tail`) does the walking. Always `return dummy.next`. If you find yourself writing `if it was the head:` while using a dummy, one pointer is doing two jobs.
- **Delete all copies:** after deleting, **don't advance** `prev`, because the new `prev.next` may be another match.
- **Search** = traversal that returns the node, index or `True` on the first match, and `None`/`-1`/`False` after the loop.

### Edge-case checklist (run this for every function)

- [ ] empty list (`head = None`)
- [ ] one node
- [ ] target is the head
- [ ] target is the tail
- [ ] target in the middle
- [ ] target not found
- [ ] duplicates / several matches
- [ ] extra pointers (tail, prev) still correct afterwards

Workflow: **make it work, make it right, make it clean**, and rerun every old test after each change (regression testing).

## 4. Doubly and circular lists

**Doubly:** each node also has `prev`. You can walk both ways and delete a node you hold in O(1), but every change must fix **two** links per side.

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev: "DNode | None" = None
        self.next: "DNode | None" = None

def delete_node(head, tail, node):    # O(1), returns new (head, tail)
    if node.prev is not None:
        node.prev.next = node.next
    else:
        head = node.next              # deleting the head
    if node.next is not None:
        node.next.prev = node.prev
    else:
        tail = node.prev              # deleting the tail
    return head, tail
```

- **Invariant to check after every operation:** for neighbours a, b: `a.next is b` **and** `b.prev is a`; `head.prev is None`; `tail.next is None`. Test with both `print_forward(head)` and `print_backward(tail)`.
- Handle each side separately (prev side, next side) with its own if/else; that covers head, tail, middle and one-node lists.

**Circular (singly):** the tail points back to the head, so there is no `None` at the end.

- Keep only `tail`: then `tail.next` is the head, giving O(1) insert at both ends.
- Insert into empty list: `new_node.next = new_node` (it points to itself).
- Insert at end: `new_node.next = tail.next; tail.next = new_node; tail = new_node`.
- **Traversal must stop with `is`**, not `is None`: start at the head and stop when you come back to it (or when `current is tail`). A plain `while current is not None` loops forever.

## 5. Reversing

In-place reversal uses three pointers and one rule: **save before you move** (store `current.next` before flipping it). O(n) time, O(1) space.

```python
def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next   # 1. save the rest
        current.next = prev        # 2. flip the arrow
        prev = current             # 3. step prev forward
        current = next_node        # 4. step current forward
    return prev                    # prev is the new head
```

- Forget step 1 and `current = current.next` follows the flipped arrow backwards: the rest of the list is lost.
- **Recursive version:** `rest = reverse(head.next)`, then `head.next.next = head; head.next = None; return rest`. Base case: empty or one node. Uses O(n) call-stack space (see the Recursive Reverse Stepper artifact).
- **Doubly reversal:** for every node swap `prev` and `next` (save `current.next` first), then swap `head` and `tail`.
- **Reversed copy** (original untouched): walk the list and `insert_front` a new node for each value into a new list. O(n) extra space.
- **Palindrome (simple):** build a reversed copy, then walk both lists comparing `.data`. O(n) space; the O(1) version is in section 6.

## 6. Fast and slow pointers

Two pointers moving at different speeds (or with a fixed gap) answer position questions in **one pass with O(1) space**.

```python
def middle(head):                     # LC 876
    slow = fast = head
    while fast is not None and fast.next is not None:   # order matters!
        slow = slow.next
        fast = fast.next.next
    return slow    # odd: the middle; even: the SECOND middle

def has_cycle(head):                  # LC 141, Floyd
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:              # check AFTER moving, with `is`
            return True
    return False

def kth_from_end(head, k):            # gap of k, one pass
    slow = fast = head
    i = 0
    while fast is not None:
        i += 1
        if i > k:
            slow = slow.next
        fast = fast.next
    if i < k:                         # list shorter than k
        return None
    return slow.data
```

- **Short-circuit evaluation:** `and` stops at the first False. `fast is not None` must come first; swapped, it crashes on even-length and empty lists with `AttributeError`.
- For the **first** middle (needed to split a list cleanly), loop on `fast.next is not None and fast.next.next is not None`.
- After k loops fast is at position 1 + 2k, so it falls off the end when slow reaches the middle.
- Inside a cycle the gap between fast and slow shrinks by 1 each loop, so fast can't jump over slow; they must meet.
- **Palindrome in O(1) space (LC 234):** find the middle, reverse the second half, compare the halves. It modifies the input (reverse the half back afterwards if the caller needs it).
- Never `print_list` a cyclic list; use a cycle-safe print (a `seen` set) when debugging.

## 7. Merging and LeetCode patterns

Most linked-list problems are a combination of a few tools; the skill is spotting which ones a problem needs.

```python
def merge_sorted(a, b):               # LC 21, O(n + m) time, O(1) space
    dummy = Node(0)
    tail = dummy                      # last node of the result
    while a is not None and b is not None:
        if a.data <= b.data:          # <= keeps equal values stable
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b   # leftovers in ONE link
    return dummy.next
```

- **Splicing:** merge re-links existing nodes instead of copying them, so the inputs are consumed (walking from a's old head now shows the merged list).
- **LeetCode format:** `ListNode` uses `.val` instead of `.data`; `Optional[ListNode]` = node or `None`; write the body inside `class Solution`. Test locally with your own `Node`, then translate.
- A runtime percentile at 0–1 ms is noise; judge by Big O.
- **Memory Limit Exceeded on a list problem** usually means you created a cycle.

| If the problem needs…              | Use                           | Example             |
| ---------------------------------- | ----------------------------- | ------------------- |
| To delete or insert at the head    | Dummy node                    | LC 19, delete value |
| To build a new list piece by piece | Dummy + tail pointer          | LC 21               |
| The node before the current one    | Trailing pointer (`prev`)     | LC 83, LC 19        |
| To reverse all or part of a list   | Three pointers                | LC 206, LC 234      |
| The middle                         | Fast/slow                     | LC 876, LC 143      |
| Cycle detection                    | Fast/slow with `is`           | LC 141              |
| The k-th from the end in one pass  | Two pointers with a gap       | LC 19               |
| Alternate front and back           | Middle + reverse half + weave | LC 143              |

## 8. Complexity and mistakes to watch

| Operation              | Singly (head only)    | Singly + tail | Doubly + tail | Array          |
| ---------------------- | --------------------- | ------------- | ------------- | -------------- |
| Access i-th element    | O(n)                  | O(n)          | O(n)          | O(1)           |
| Insert at front        | O(1)                  | O(1)          | O(1)          | O(n)           |
| Insert at end          | O(n)                  | O(1)          | O(1)          | O(1) amortized |
| Delete front           | O(1)                  | O(1)          | O(1)          | O(n)           |
| Delete end             | O(n)                  | O(n)          | O(1)          | O(1)           |
| Delete a node you hold | O(n)                  | O(n)          | O(1)          | O(n)           |
| Search by value        | O(n)                  | O(n)          | O(n)          | O(n)           |
| Reverse in place       | O(n) time, O(1) space | same          | same          | same           |

**Mistakes I made during this topic (check these first):**

- Overwriting `.next` before saving the rest of the list (save before you move).
- Wrong loop condition order: `fast.next` checked before `fast`.
- Moving the `dummy` itself, which brought back the head special case.
- Missing the constraint in the question ("one pass", "return the value", "don't modify the list").
- Writing a condition that fits one test (`k - i == 1`) instead of describing the problem (`i < k`). Test with values that are not in the question.
- A function that only asks a question about a list (k-th from end) must never modify it; print the list after the call to prove it.
- Output that contradicts my own claim: check that the test I print actually demonstrates what I say.
- Two halves sharing a node in Reorder List: a self-link becomes a cycle (Memory Limit Exceeded).
