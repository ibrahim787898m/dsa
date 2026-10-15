# Linked List — Practice Questions

Oct 15, 2026 · @Ibrahim Mustafa Opu

## How to use this

Re-solve every question from scratch, without opening your old answers in `quiz/lesson_N.md` until you're done. Tick a box only when the code runs and every listed case passes.

- Workflow: trace or code → run it → check every part of the question → then compare with your old answer.
- For code questions, build each test list by hand and print the list before and after the call.
- Questions marked ★ were the ones that took more than one try the first time; do those first.

## Quiz questions: Lessons 1–4

### Lesson 1: Basics

- [ ] **L1 Q1.** Why is accessing the 5th element O(1) in an array but O(n) in a linked list? Explain it in terms of memory.
- [ ] **L1 Q2.** What does this print, and what happens to the node holding 10?

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

- [ ] **L1 Q3.** Write `length(head)` that returns the number of nodes (0 for an empty list).
- [ ] **L1 Q4.** You constantly add items to the front and almost never look items up by position. Array or linked list? Why?
- [ ] **L1 Q5.** This loop has a bug. What is it, and what happens on a 3-node list and on an empty list?

```python
current = head
while current.next is not None:
    print(current.data)
    current = current.next
```

### Lesson 2: Insertion

- [ ] **L2 Q1.** Starting from `head = None`, what is the list after: `insert_front(1)`, `insert_end(2)`, `insert_front(3)`, `insert_at(index 1, value 4)`?
- [ ] **L2 Q2 ★.** Start with `4 -> 8 -> 6`, `a = [4]`, `new_node = Node(5)`. Someone runs `a.next = new_node` then `new_node.next = a.next`. Draw the list after each line. What does a traversal from \[4\] print? Which nodes are lost?
- [ ] **L2 Q3 ★.** Trace and give the exact output:

```python
head = Node(2)
head = insert_end(head, 4)
insert_front(head, 9)          # result not assigned!
head = insert_front(head, 1)
current = head
while current:
    print(current.data)
    current = current.next
```

- [ ] **L2 Q4 ★.** Write `insert_end` using `while current is not None` instead of `while current.next is not None`. Can it work? If yes, how (hint: a trailing pointer)? If not, why not?
- [ ] **L2 Q5 ★.** Keep `head` and `tail`. Write `insert_end_fast(head, tail, data)` and `insert_front_fast(head, tail, data)`, both O(1), both returning `(head, tail)`. Test on an empty list, one node, and three nodes.

### Lesson 3: Deletion, search, dummy node

- [ ] **L3 Q1.** Using the dummy-node `delete_value`, trace `delete_value(head, 6)` on `6 -> 2 -> 6 -> 8`. What is returned? Then trace `delete_value(head, 5)` on the same list.
- [ ] **L3 Q2.** Write `delete_last(head)` without a tail variable. Test on `3 -> 7 -> 1`, one node, and an empty list.
- [ ] **L3 Q3 ★.** This tries to delete every node equal to target. Trace it on `1 -> 3 -> 3 -> 5` (target 3) and on `1 -> 3` (target 3). Find both bugs, fix it, and run it.

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

- [ ] **L3 Q4.** Write `index_of(head, target)`: index of the first match, or -1. Test: found at head, found in the middle, not found, empty list.
- [ ] **L3 Q5 ★.** Write `delete_value_fast(head, tail, target)` returning `(head, tail)`. When must tail change? Test deleting the last node, the only node, a middle node, and a value with duplicates; print tail after each.

### Lesson 4: Doubly and circular

- [ ] **L4 Q1.** Start with `1 <-> 2 <-> 4`. Insert 3 after \[2\] with the four lines below but skip line 3. Draw the result. What do forward and backward traversals print?

```python
new_node.prev = node
new_node.next = node.next
node.next.prev = new_node      # line 3 (skipped)
node.next = new_node
```

- [ ] **L4 Q2.** Write `check(head, tail)` that returns True only if the doubly list is consistent: empty → both None; `head.prev is None`, `tail.next is None`; every `node.next.prev is node`; walking forward from head ends at tail.
- [ ] **L4 Q3 ★.** Write `insert_after(head, tail, node, data)` returning `(head, tail)`. Test: node in the middle, node is the tail, node is the only node. Run `check()` after each.
- [ ] **L4 Q4.** For this shorter `delete_node`, say for each case (middle, head, tail, only node) whether it works, crashes (on which line), or leaves head/tail wrong. Then write the correct version.

```python
def delete_node(head, tail, node):
    node.prev.next = node.next
    node.next.prev = node.prev
    return head, tail
```

- [ ] **L4 Q5.** Circular singly list with only `tail`. Write `insert_end_circ(tail, data)` (returns the new tail) and `print_circ(tail)` (prints every value once, starting from the head). Test on empty, one node, three nodes.

## Quiz questions: Lessons 5–7

### Lesson 5: Reversing

- [ ] **L5 Q1.** Trace `reverse()` (three pointers) on `5 -> 8`. Show `next_node`, what got flipped, `prev`, `current` and the picture after each pass. What does it return?
- [ ] **L5 Q2.** Trace this on `1 -> 2 -> 3 -> 4`. How many passes run? What list is returned? Which nodes are lost? In one sentence, what's the bug in terms of save-before-you-move?

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

- [ ] **L5 Q3.** Write `reverse(head)` from the three-pointer idea, without looking. Test: empty, one node, two nodes, `1 -> 2 -> 3 -> 4 -> 5`.
- [ ] **L5 Q4 ★.** Write `reverse_doubly(head, tail)` returning `(head, tail)`: swap prev/next in every node, then swap the ends. Careful: after the swap, `current.next` points backwards. Test: empty, one node, three nodes, with `check()`, `print_forward` and `print_backward`.
- [ ] **L5 Q5 ★.** Write `reversed_copy(head)` (original unchanged) and `is_palindrome(head)`. Tests: empty → True, \[7\] → True, \[1,2,2,1\] → True, \[1,2,3,2,1\] → True, \[1,2\] → False, \[1,2,3\] → False.

### Lesson 6: Fast and slow pointers

- [ ] **L6 Q1.** Trace `middle()` on `1 -> … -> 7` and on `1 -> … -> 6`. For even lengths, does it return the first or the second middle?
- [ ] **L6 Q2.** The loop condition is swapped to `while fast.next is not None and fast is not None:`. Trace it on `1 -> 2 -> 3`, `1 -> 2 -> 3 -> 4` and an empty list. Which crash, on which check, with which exact error? Why does the order matter?
- [ ] **L6 Q3.** Write `has_cycle(head)` with fast/slow (no set). Tests: empty F, one node F, one node pointing to itself T, `1 -> 2 -> 3 -> 4` F, same with 4 → 1 T, `1 -> … -> 5` with 5 → 3 T.
- [ ] **L6 Q4 ★.** Write `kth_from_end(head, k)` returning the **value**, in **one pass**, without modifying the list. On `10 -> 20 -> 30 -> 40 -> 50`: k=1 → 50, k=2 → 40, k=5 → 10, k=6 → None, k=7 → None; empty with k=1 or k=2 → None. Print the list after the call.
- [ ] **L6 Q5.** Write `is_palindrome_fast(head)` with O(1) extra space (middle + reverse second half + compare). Same six tests as L5 Q5. Does it modify the list? (Print it after calling on `1 -> 2 -> 3`.) What's the trade-off vs L5 Q5?

### Lesson 7: Merge and LeetCode

- [ ] **L7 Q1.** Trace `merge_sorted()` on `a = 1 -> 4 -> 5`, `b = 2 -> 3 -> 6`. What does it return? Walking from a's old head afterwards, what do you see and **why** (copied or re-linked)? What happens if `a` is empty?
- [ ] **L7 Q2. LC 21 Merge Two Sorted Lists.** Tests: both empty; a empty; b empty; `1->3->5` + `2->4->6`; `1->2->2` + `2->3`; `1` + `2->3->4->5`.
- [ ] **L7 Q3. LC 83 Remove Duplicates from Sorted List.** Tests: empty; `1`; `1->1->2`; `1->1->1`; `1->1->2->3->3`; `1->2->3`.
- [ ] **L7 Q4 ★. LC 19 Remove Nth Node From End.** One pass, dummy node that never moves, no head special case. Tests: `1->2->3->4->5` n=2; `1` n=1; `1->2` n=1; `1->2` n=2.
- [ ] **L7 Q5 ★. LC 143 Reorder List.** Write the plan first (which tools, in what order, why). Tests: `1`; `1->2`; `1->2->3->4` → `1->4->2->3`; `1->2->3->4->5` → `1->5->2->4->3`. Bonus: split so the halves share no node (no guard needed).

## Extra practice (new questions)

These are new and ordered roughly easy → hard. Each one reuses a tool from the notes; write the edge cases yourself before coding.

- [ ] **E1. Count matches.** `count(head, value)` returns how many nodes hold `value`.
- [ ] **E2. Sum and max.** `total(head)` and `max_value(head)` (return `None` for an empty list).
- [ ] **E3. Nth node.** `get(head, i)` returns the value at index i, or `None` if i is out of range (including negative i).
- [ ] **E4. Build and print.** `from_list([1, 2, 3])` builds a linked list from a Python list; `to_list(head)` turns it back. Use them to make all future tests one line.
- [ ] **E5. Insert into a sorted list.** `insert_sorted(head, value)` keeps the list sorted. Test: empty, smaller than head, larger than tail, middle, duplicate value.
- [ ] **E6. Delete at index.** `delete_at(head, i)` with a dummy node. Test i = 0, last index, middle, out of range.
- [ ] **E7. Are two lists equal?** `equal(a, b)` compares values position by position. Test different lengths.
- [ ] **E8. Second-to-last node.** Return the value of the second-to-last node in one pass, no length count.
- [ ] **E9. Reverse the first k nodes.** `reverse_first_k(head, k)`: `1->2->3->4->5`, k=3 → `3->2->1->4->5`. What if k > length?
- [ ] **E10. Split odd/even positions.** Return two lists: nodes at positions 0, 2, 4… and 1, 3, 5… (re-link nodes, don't copy).
- [ ] **E11. Rotate right by k.** `1->2->3->4->5`, k=2 → `4->5->1->2->3`. Handle k larger than the length.
- [ ] **E12. Cycle start.** If `has_cycle` finds a meeting point, find the node where the cycle begins (hint: after they meet, reset one pointer to head and move both one step at a time).
- [ ] **E13. Doubly: remove all of a value.** `remove_all(head, tail, value)` on a doubly list, returning `(head, tail)`, with `check()` after each test (all nodes match, first and last match, none match).
- [ ] **E14. Circular: delete a value.** On a tail-only circular list, delete the first node holding `value` and return the new tail. Test: only node, the tail node, the head node, not found.
- [ ] **E15. Restore after palindrome.** Change `is_palindrome_fast` so the list is exactly as before when the function returns. Prove it by printing the list after the call.

## Extra LeetCode problems

Work top to bottom; each row names the tool from the concept notes it needs. Already solved in the quizzes: 21, 83, 19, 143.

| #   | Problem                                                                                                       | Difficulty | Pattern                               | Done |
| --- | ------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------- | ---- |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)                                     | Easy       | Three pointers (also try recursive)   |      |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)                         | Easy       | Fast/slow                             |      |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)                                         | Easy       | Fast/slow with `is`                   |      |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)                     | Easy       | Dummy node, delete all                |      |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                               | Easy       | Middle + reverse half + compare       |      |
| 160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)           | Easy       | Two pointers, `is`                    |      |
| 237 | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)                   | Medium     | Copy next value, skip next            |      |
| 2   | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                             | Medium     | Dummy + tail, carry                   |      |
| 24  | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)                                     | Medium     | Dummy + save before you move          |      |
| 61  | [Rotate List](https://leetcode.com/problems/rotate-list/)                                                     | Medium     | Length, make circular, cut            |      |
| 82  | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Medium     | Dummy + trailing pointer              |      |
| 86  | [Partition List](https://leetcode.com/problems/partition-list/)                                               | Medium     | Two dummy + tail lists                |      |
| 92  | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)                               | Medium     | Dummy + partial reverse               |      |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)                                   | Medium     | Floyd: find cycle start               |      |
| 328 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)                                   | Medium     | Two chains, re-link                   |      |
| 707 | [Design Linked List](https://leetcode.com/problems/design-linked-list/)                                       | Medium     | Everything from Lessons 1–3           |      |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/)                                                         | Medium     | Middle + merge (merge sort)           |      |
| 23  | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)                                   | Hard       | Merge, repeated or divide and conquer |      |
| 25  | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)                           | Hard       | Dummy + partial reverse, repeated     |      |

Problem numbers and difficulties are as I know them, not checked live; LeetCode occasionally re-rates difficulty.
