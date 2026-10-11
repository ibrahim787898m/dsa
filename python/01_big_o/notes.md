# Big O Notation: Notes

Sep 27, 2026 · Ibrahim Mustafa Opu

## 1. What Big O measures

Big O describes how an algorithm's work (time) or memory (space) grows as the input size n grows. It answers one question: when n gets bigger, how fast does the cost grow?

- It ignores machine speed, language and constant factors.
- It describes growth, not speed. An O(1) operation can still be slow; it just doesn't get slower as n grows.
- It usually describes the worst case, which is what interviews and LeetCode mean by "the complexity".
- It matters most when data grows. O(n²) on 100 items is instant; on a million items it breaks.

## 2. The growth ladder

Fastest to slowest. "Max n" is a rule of thumb for what runs in about 1 second (roughly 10⁸ simple operations).

| Complexity | Name | Typical example | Steps at n = 1,000 | Max n in ~1 s |
| --- | --- | --- | --- | --- |
| O(1) | Constant | Index into a list, dict lookup, append/pop at end | 1 | any |
| O(log n) | Logarithmic | Binary search, halving the problem each step | ~10 | 10¹⁸ |
| O(√n) | Square root | Checking if a number is prime | ~32 | 10¹⁶ |
| O(n) | Linear | One pass over an array, linear search, two pointers | 1,000 | 10⁸ |
| O(n log n) | Linearithmic | Merge sort, Python's sort() | ~10,000 | 10⁶–10⁷ |
| O(n²) | Quadratic | Nested loops over the same input, bubble sort | 1,000,000 | 10⁴ |
| O(n³) | Cubic | Three nested loops | 10⁹ | ~500 |
| O(2ⁿ) | Exponential | All subsets, naive recursive Fibonacci | ~10³⁰¹ | ~25 |
| O(n!) | Factorial | All permutations | ~10²⁵⁶⁷ | ~11 |

### Each complexity, with an example

#### O(1): Constant

The work stays the same no matter how big the input is.

```python
def get_first(nums):
    return nums[0]
```

Why: indexing jumps straight to a memory address. A list of 10 or 10 million items takes one step.

```python
# Array
nums = [1, 2, 3]
nums.append(4)    # push to end
nums.pop()        # pop from end
nums[0]           # lookup
nums[1]
nums[2]


# HashMap / Set
hashMap = {}
hashMap["key"] = 10     # insert
print("key" in hashMap) # lookup
print(hashMap["key"])   # lookup
hashMap.pop("key")      # remove
```

#### O(log n): Logarithmic

A logarithmic algorithm repeatedly reduces the problem size, commonly by half. Binary search is the classic example.

```text
n → n/2 → n/4 → n/8 → ... → 1
```

```python
def binary_search(nums, target):   # nums is sorted
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

Why: each check throws away half of what's left. After k steps, n / 2ᵏ items remain, so it ends after log₂ n steps. For 1,000,000 items, that's about 20 steps. Real life: finding a word in a dictionary by opening it in the middle.

```python
# Binary search
nums = [1, 2, 3, 4, 5]
target = 6
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if target < nums[m]:
        r = m - 1
    elif target > nums[m]:
        l = m + 1
    else:
        print(m)
        break

# Binary Search on BST
# O(log n) only if the tree is balanced.
# A lopsided tree (like a linked list) is O(n).
def search(root, target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    else:
        return True

# Heap Push and Pop: O(log n) each
import heapq
minHeap = []
heapq.heappush(minHeap, 5)
heapq.heappop(minHeap)
```

#### O(√n): Square root

The loop runs until i² reaches n.

```python
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
```

Why: if n has a factor bigger than √n, it must also have one smaller than √n, so checking up to √n is enough. For n = 1,000,000, that's about 1,000 checks.

#### O(n): Linear

The work grows in step with the input. Double n, double the work.

```python
def find_max(nums):
    best = nums[0]
    for x in nums:
        if x > best:
            best = x
    return best
```

Why: you must look at every element once, because the maximum could be anywhere. Real life: reading every name on an unsorted list to find someone.

```python
nums = [1, 2, 3]
sum(nums)           # sum of array
for n in nums:      # looping
    print(n)

nums.insert(1, 100) # insert middle
nums.remove(100)    # remove middle
print(100 in nums)  # search

import heapq
heapq.heapify(nums) # build heap

# sometimes even nested loops can be O(n)
# (e.g. monotonic stack or sliding window)
```

#### O(n log n): Linearithmic

Conceptually, this is n work across log n levels. It commonly appears in efficient sorting algorithms such as merge sort and heap sort, and in average-case quicksort.

```text
n work × log n levels = O(n log n)
```

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)   # merging is O(n)
```

Why: the list is halved log n times, and each level of halving does n work to merge. n × log n. This is the best possible for sorting by comparisons, and it's what Python's sort() does.

```python
# HeapSort
import heapq
nums = [1, 2, 3, 4, 5]
heapq.heapify(nums)         # O(n), once
while nums:                 # runs n times
    heapq.heappop(nums)     # O(log n) each
# total: O(n) + n × O(log n) = O(n log n)

# MergeSort and Python's sorted() / list.sort() are also O(n log n)
```

#### O(n²): Quadratic

For every item, you do something with every other item.

```python
def has_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

Why: comparing every pair gives n(n−1)/2 comparisons. Double n, and the work goes up 4×. Real life: everyone in a room shaking hands with everyone else.

```python
# Traverse a square grid
# O(n²) when n is the side length (n rows × n columns).
# If n means the total number of cells, the same loop is O(n).
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])

# Get every pair of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])

# Insertion sort (insert in middle n times -> n^2)
```

#### O(n³): Cubic

Three nested loops over the input.

```python
def count_zero_triples(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    count += 1
    return count
```

Why: every triple of items is checked. Double n, and the work goes up 8×.

#### O(2ⁿ): Exponential

Each step branches into two, and the branches keep branching. A classic example is naive recursive Fibonacci.

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Why: every call makes two more calls, so the number of calls roughly doubles each level, n levels deep. Adding 1 to n doubles the work. fib(40) makes over 300 million calls. Generating all subsets of n items is also O(2ⁿ), since each item is either in or out.

```python
# Recursion, tree height n, two branches
def recursion(i, nums):
    if i >= len(nums):      # >= not ==, because i + 2 can jump past len(nums)
        return 0
    branch1 = recursion(i + 1, nums)
    branch2 = recursion(i + 2, nums)
    return branch1 + branch2  # without a return, the result is lost
```

#### O(n!): Factorial

Trying every possible ordering.

```python
def permutations(items):
    if len(items) <= 1:
        return [items]
    result = []
    for i in range(len(items)):
        rest = items[:i] + items[i + 1:]
        for p in permutations(rest):
            result.append([items[i]] + p)
    return result
```

Why: n choices for the first spot, n−1 for the second, and so on: n × (n−1) × … × 1 = n!. 10 items give 3,628,800 orderings; 20 items give about 2.4 × 10¹⁸. Real life: trying every route through n cities.

## 3. Simplification rules

Count the steps, then keep only what dominates as n gets huge.

1. **Drop constants.** O(2n), O(n/2) and O(100n) are all O(n).
2. **Drop smaller terms.** O(3n² + 5n log n + 1000) → O(n²). At n = 1,000 the n² term is 3,000,000; the others are about 50,000 and 1,000.
3. **Steps one after another add.** Two separate loops over n = O(n + n) = O(n), not O(n²).
4. **Nested steps multiply.** A loop of n inside a loop of n = O(n × n) = O(n²).
5. **Different inputs get different letters.** Loop over a, then b = O(a + b). Nested = O(a × b).
6. **Log base doesn't matter.** log₂ n and log₃ n differ only by a constant, so both are O(log n).
7. **A loop over a fixed number is O(1).** 26 letters, 10 digits, 4 directions don't grow with n.

Notation: write n² or n^2. n\*2 means 2n, which is O(n).

## 4. Finding complexity from code

Go line by line. A line costs O(1) unless it hides a loop. Then combine with the rules above.

### The k-steps method for loops

1. Write what the loop variable equals after k iterations.
2. Set it equal to the stopping condition.
3. Solve for k. That's the number of iterations.

| Loop | After k steps | Solve | Result |
| --- | --- | --- | --- |
| i += 1 until n | i = k | k = n | O(n) |
| i += 2 until n | i = 2k | k = n/2 | O(n) |
| i \*= 2 until n | i = 2ᵏ | k = log₂ n | O(log n) |
| i \*= 3 until n | i = 3ᵏ | k = log₃ n | O(log n) |
| i //= 2 from n to 1 | i = n / 2ᵏ | k = log₂ n | O(log n) |
| i += 1 while i \* i < n | i = k | k = √n | O(√n) |

What a log means: log₃ n is how many times you multiply by 3 to reach n, or divide n by 3 to reach 1. Adding a constant each step → O(n). Multiplying or dividing by a constant → O(log n).

Trace with the exact operator. i \*= 3 goes 1, 3, 9, 27, 81, 243. It does not go 3, 27, 19683 (that would be i = i \*\* 3).

### Nested loops: add up the inner work

When the inner loop depends on the outer one, sum its work across all outer iterations:

```python
for i in range(n):
    for j in range(i, n):
        ...
```

n + (n−1) + … + 1 = n(n+1)/2 → O(n²).

### Recursion: count calls × work per call

- One recursive call that shrinks n by 1 (sum_to(n−1)) → n calls → O(n).
- One call that halves n (binary search) → log n calls → O(log n).
- Two calls that each shrink n by 1 (naive fib) → the calls double each level → O(2ⁿ).

### Bigger code

Split it into parts, find each part's cost, then add sequential parts and multiply nested ones. The biggest part is the bottleneck and the only one worth optimizing. Example: sort (n log n) + loop of n that calls a list search (n) = O(n log n + n²) = O(n²). Fix the search.

## 5. Space complexity

Count the extra memory your code allocates (auxiliary space). The input itself usually isn't counted.

| Code | Extra space | Why |
| --- | --- | --- |
| A few variables (lo, hi, count) | O(1) | Size doesn't depend on n |
| A new list, set or dict of up to n items | O(n) | Grows with the input |
| An n × n grid | O(n²) | n rows of n |
| Recursion n levels deep | O(n) | Each waiting call is a stack frame |
| Recursion log n levels deep (binary search) | O(log n) | Depth halves each call |

Old objects that are thrown away (like the old string in result = ch + result) are freed, so they don't add up. Space counts what exists at the same time.

**Time–space trade-off:** spending O(n) memory on a set or dict often turns O(n²) time into O(n). This is the most common optimization in array problems.

## 6. Best, average and worst cases

The symbols describe bounds on growth. The cases describe which input you feed in. They are separate ideas.

| Symbol | Name | Meaning |
| --- | --- | --- |
| O | Big O | Upper bound: grows no faster than this ("at most") |
| Ω | Big Omega | Lower bound: grows at least this fast ("at least") |
| Θ | Big Theta | Tight bound: O and Ω match ("exactly this rate") |

CS50 uses O for the worst case and Ω for the best case. In interviews, "the complexity" means worst-case Big O.

| Algorithm | Best | Average | Worst | Extra space | Note |
| --- | --- | --- | --- | --- | --- |
| Linear search | Ω(1) | O(n) | O(n) | O(1) | Works on unsorted data |
| Binary search | Ω(1) | O(log n) | O(log n) | O(1) | Needs sorted data |
| Bubble sort | Ω(n) | O(n²) | O(n²) | O(1) | Best case with early exit |
| Selection sort | Ω(n²) | O(n²) | O(n²) | O(1) | Always scans the rest |
| Insertion sort | Ω(n) | O(n²) | O(n²) | O(1) | Fast on nearly sorted data |
| Merge sort | Ω(n log n) | O(n log n) | O(n log n) | O(n) | Θ(n log n) |
| Quick sort | Ω(n log n) | O(n log n) | O(n²) | O(log n) | Worst case with bad pivots |
| Hash lookup | Ω(1) | O(1) | O(n) | O(n) | Worst case with many collisions |

## 7. Python operation costs

Many Python one-liners hide a loop. Inside another loop, they multiply.

| Operation | Cost | Watch out |
| --- | --- | --- |
| lst[i], lst[i] = x, len(lst) | O(1) | |
| lst.append(x), lst.pop() | O(1) | append is amortized O(1) |
| lst.pop(0), lst.insert(0, x) | O(n) | Shifts every element; use collections.deque |
| x in lst, lst.index(x), lst.count(x) | O(n) | In a loop this becomes O(n²) |
| x in set, d[key], key in d | O(1) | Average case |
| lst[a:b], s[a:b], lst.copy() | O(k) | Slicing copies k elements |
| sorted(lst), lst.sort() | O(n log n) | |
| min, max, sum | O(n) | |
| s += c or s = c + s in a loop | O(n²) total | Strings are immutable; each + copies the whole string |
| "".join(parts), s[::-1], s.split() | O(n) | |

### Why string + in a loop is O(n²)

```python
result = ""
for ch in s:
    result = ch + result
```

Each + builds a new string and copies all of result. The copies are 1 + 2 + … + n = n(n+1)/2 → O(n²). Collect characters in a list and "".join() once at the end, or use s[::-1].

## 8. Reading constraints and choosing an approach

The size of n tells you which complexity you need before you write any code. Plug n into each candidate and compare it with about 10⁸ operations per second.

Example, n ≤ 10⁵: O(n²) = 10¹⁰ operations ≈ 100 seconds, so it fails. O(n log n) ≈ 1.7 × 10⁶ and O(n) = 10⁵ both fit.

Aim for the slowest complexity that fits, not the fastest one you know. O(log n) is usually impossible on an unsorted array, because reading the input once is already O(n).

### The approach

1. Read the constraints and work out the target complexity.
2. Write the brute-force solution and find its complexity.
3. Find the repeated work: what are you recomputing or searching again and again?
4. Pick a tool that removes it.

| Repeated work | Common fix | Typical gain |
| --- | --- | --- |
| Searching a list again and again | Hash set or hash map | O(n²) → O(n) |
| Comparing every pair | Sort, then two pointers | O(n²) → O(n log n) |
| Recomputing sums of ranges | Prefix sums | O(n²) → O(n) |
| Searching sorted data | Binary search | O(n) → O(log n) |
| Solving the same subproblem again | Memoization or dynamic programming | O(2ⁿ) → O(n) |

### In real software

- Correct and readable first; optimize once something is actually slow.
- Measure with a profiler (cProfile in Python) instead of guessing.
- Most real slowness is I/O: a database query or network call inside a loop has the same shape as x in lst inside a loop.

## 9. Quick Complexity Recognition

| Look for... | Likely complexity |
| --- | --- |
| Direct access such as arr[i] | O(1) |
| One pass through input | O(n) |
| Two loops nested together | Often O(n²) |
| Problem repeatedly cut in half | O(log n) |
| Separate loops over A and B | O(a + b) |
| Nested loops over A and B | O(ab) |
| Recursion | Analyze number/size of recursive calls |

## 10. Core Cheat Sheet — Memorize This

```text
O(1)        Constant      → Same amount of work
O(log n)    Logarithmic   → Repeatedly divide problem
O(n)        Linear        → Go through input once
O(n log n)  Linearithmic  → Common in efficient sorting
O(n²)       Quadratic     → Often nested loops
O(2ⁿ)       Exponential   → Grows extremely fast

RULES
O(2n) → O(n)
O(n² + n) → O(n²)
Sequential: O(n) + O(n) → O(n)
Nested:     O(n) × O(n) → O(n²)

SPACE
A few variables       → O(1)
New structure of size n → O(n)

CASES
Best    → Most favorable input
Average → Typical/expected behavior
Worst   → Most costly input
```

## 11. Mistakes to avoid

These came up in your self-check quiz.

| Mistake | Correct thinking |
| --- | --- |
| Counting count += 1 as O(m) | Plain arithmetic, assignment and indexing are O(1). Only lines that hide a loop cost more. |
| Tracing i \*= 3 as 3, 27, 19683 | Trace the exact operator: 1, 3, 9, 27, 81, 243. |
| "One loop, so O(n)" | Check every line inside the loop for hidden work, like string + or x in lst. |
| Writing O(n\*2) for n squared | Write O(n²) or O(n^2). n\*2 is 2n. |
| "It'll probably be too slow" | Do the arithmetic: n² at n = 10⁵ is 10¹⁰, about 100 seconds. |
| Aiming for O(log n) by default | Aim for the slowest complexity that fits the constraints. |
| Two separate loops = O(n²) | Sequential loops add: O(n + n) = O(n). |
| Two inputs of different sizes = O(n²) | Use two letters: O(m × n). |

## 12. Recommended Learning Order

1. Understand n
2. O(1)
3. O(n)
4. O(n²)
5. O(log n)
6. O(n log n)
7. Big-O simplification rules
8. Space complexity
9. Best / Average / Worst case
10. Analyze actual Python code
11. Data structure complexities
12. Recursion + Big-O

**Teacher tip:** Don't try to memorize everything at once. First become comfortable identifying O(1), O(n), and O(n²) from simple Python code. Then move to logarithmic complexity, space complexity, and more advanced analysis.

---

Big-O is about growth, not exact seconds. The goal is to recognize the pattern in the code and explain why the complexity has that growth rate.
