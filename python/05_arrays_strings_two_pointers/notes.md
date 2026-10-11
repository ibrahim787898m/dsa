# DSA Notes: Arrays, Strings & Two Pointers

## Lesson 1: Arrays

An array stores elements side by side in memory, so reading any index is O(1). Inserting or removing anywhere except the end is O(n). In Python, a list is a dynamic array (the same thing as a C++ `vector`).

### Why `arr[i]` is O(1)

The computer does not remember where each element is. It **calculates** the address:

```math
\text{address}(i) = \text{start} + i \times \text{element size}
```

That is one multiplication and one addition, the same work for `arr[0]` and `arr[500]`. This only works because the elements are **side by side**. In a linked list the elements are scattered, so reaching index i is O(n).

### Why inserting at the front is O(n)

Every existing element must shift one place right to make room. With n elements, that's n moves. `arr.pop(0)` is the same in reverse: every element shifts left. Adding or removing at the **end** moves nothing, so it's O(1).

**Replace is not insert.** `arr[0] = x` overwrites one slot: nothing shifts, O(1). `arr.insert(0, x)` adds a slot: everything shifts, O(n).

### Operation costs (memorize)

| Operation | Python | Time |
| --- | --- | --- |
| Read or replace by index | `arr[i]`, `arr[i] = x` | O(1) |
| Add to end | `arr.append(x)` | O(1) amortized |
| Remove from end | `arr.pop()` | O(1) |
| Insert or remove at front or middle | `arr.insert(0, x)`, `arr.pop(0)` | O(n) |
| Search | `x in arr`, `arr.index(x)`, `arr.count(x)`, `arr.remove(x)` | O(n) |
| Slice (copy) | `arr[a:b]` | O(b − a) |
| Join two lists | `a + b` | O(len(a) + len(b)) |
| Sort | `arr.sort()`, `sorted(arr)` | O(n log n) |

**Amortized O(1):** now and then Python moves the whole list to a bigger block of memory, but averaged over many appends it's O(1).

**Hidden loops:** `in`, `.index()`, `.count()`, `.remove()`, slicing and `+` look like one step but loop inside. A `x in arr` inside a `for` loop is O(n²).

### Need fast adds or removes at the front?

Use `collections.deque`: `appendleft(x)` and `popleft()` are both O(1). You'll use it for queues and BFS later.

### Pattern: single pass

```python
# Time: O(n) | Space: O(1)
def count_evens(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:      # % is remainder; / is division
            count += 1
    return count

print(count_evens([1, 2, 3, 4]))  # 2
print(count_evens([]))            # 0
```

### Big O rules from this lesson

- **Space counts only the extra memory your code creates.** The input doesn't count. One counter variable = O(1); a new list that grows with n = O(n).
- **Add** steps that happen one after another: `n × (O(1) + O(1)) = O(n)`.
- **Multiply** only when one thing is inside another (a loop inside a loop).
- Always finish with the Big O: drop constants and smaller terms.

## Lesson 2: Strings

A string is an array of characters, so `s[i]` and `len(s)` are O(1) and a loop over it is O(n). The big difference: Python strings are **immutable**, so every "change" builds a new string in O(n).

### Immutable

```python
s = "hello"
s[0] = "j"          # TypeError: strings can't be changed
s = "j" + s[1:]     # builds a NEW string "jello", O(n)
```

Immutability is a **design choice** by Python's creators, not about fixed or dynamic size. One reason: a string that never changes is safe to use as a dict key.

### The trap: building a string in a loop

```python
result = ""
for ch in s:
    result += ch      # copies all of result every time
```

Each `+=` copies everything built so far: 1, 2, 3 … n characters. The total is a **sum**:

```math
1 + 2 + \dots + n = \frac{n(n+1)}{2} \rightarrow O(n^2)
```

**Rule:** when each iteration costs the **same** (c), total = n × c. When the cost **grows** each iteration, total = the **sum** of the costs. Don't multiply that sum by n again, because it already covers every iteration. Check sums with a small n (n = 3: 2 + 4 + 6 = 12 = 3 × 4).

### The fix: list, then join once

```python
# Time: O(n) | Space: O(n)
def repeat(s):
    parts = []
    for ch in s:
        parts.append(ch + ch)   # O(1) each
    return "".join(parts)       # O(n) once

print(repeat("abc"))  # aabbcc
```

Space is O(n) here because the output itself is 2n long. That can't be avoided.

### Operation costs

| Operation | Example | Time |
| --- | --- | --- |
| Access a char | `s[i]` | O(1) |
| Length | `len(s)` | O(1) |
| Slice or reverse (copy) | `s[a:b]`, `s[::-1]` | O(k) |
| Search | `"lo" in s`, `s.find("lo")` | O(n) typical |
| Join | `"".join(parts)` | O(total length) |
| Split | `s.split(" ")` | O(n) |
| Lowercase | `s.lower()` | O(n), new string |
| Check one char | `ch.isalnum()`, `ch.isdigit()` | O(1) |
| Char ↔ number | `ord("a")` → 97, `chr(97)` → "a" | O(1) |

### Pattern: counting characters with a dict

Dict lookups and updates are O(1) on average, so counting is O(n). `x in some_dict` is O(1); `x in some_list` is O(n). Same syntax, very different cost.

```python
# Time: O(n) | Space: O(k), k = distinct chars (≤ 26 lowercase letters → often called O(1))
def is_anagram(a, b):
    if len(a) != len(b):         # needed for correctness, not just speed
        return False
    count = {}
    for ch in a:
        count[ch] = count.get(ch, 0) + 1
    for ch in b:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True

print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))        # False
print(is_anagram("aab", "abb"))        # False
```

Without the length check, `is_anagram("ab", "a")` would wrongly return True. The sorting version, `sorted(a) == sorted(b)`, also works but is O(n log n) time and O(n) space.

## Lesson 3: Two Pointers

Two indexes that move by a rule often turn an O(n²) brute force into O(n) time with O(1) space. There are 3 patterns. For each one, what matters most is the **exact rule for moving each pointer**.

### Pattern 1: Opposite ends, moving inward

Left starts at 0, right at the end, and they move toward each other until they meet.

```python
# Time: O(n) | Space: O(1)
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

Compare with `s[::-1] == s`: also O(n) time, but O(n) space because it builds a reversed copy.

**Two Sum II (#167): sorted array, find a pair that adds up to target.**

```python
# Time: O(n) | Space: O(1)
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left + 1, right + 1]   # LeetCode #167 wants 1-based indexes
        elif total < target:
            left += 1
        else:
            right -= 1
    return []
```

**Why skipping is safe (say it this precisely):** nums[left] is the **smallest** remaining value. If even nums[left] + nums[right] is too big, then nums[right] plus any larger value is too big too. So nums[right] can't be in any answer: remove it. The mirror case: if the total is too small, nums[left] can't be in any answer. Each step removes one element for good, so it takes at most n steps: O(n).

**Why it needs sorted order:** the argument depends on nums[left] being the smallest and nums[right] the biggest. On `[1, 4, 2]` with target 5 (answer 1 + 4): 1 + 2 = 3 is too small, so the algorithm throws away 1, assuming 2 was the biggest. It wasn't (4 is), so the answer is missed and it returns [].

**Unsorted → use a dict (Two Sum #1).**

```python
# Time: O(n) | Space: O(n)
def two_sum(nums, target):
    seen = {}                      # value → index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

### Pattern 2: Same direction, slow and fast

`fast` looks at every element. `slow` marks where the next element you **keep** gets written. Use it to change an array in place with O(1) space.

```python
# Remove all copies of val. Compare with VAL.
# Time: O(n) | Space: O(1)
def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

# Remove duplicates from a SORTED array. Compare with NUMS[SLOW].
# Time: O(n) | Space: O(1)
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

# Move zeroes: swap instead of copy, so the zeros drift to the end.
# Time: O(n) | Space: O(1)
def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):      # start at 0, NOT 1
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeroes([0]))               # [0]
print(move_zeroes([1, 2]))            # [1, 2]
```

### Pattern 3: Two arrays, one pointer each

Compare `a[i]` with `b[j]` and move the pointer at the **smaller** value. The pointers do not move in lockstep.

```python
# Time: O(n + m) | Space: O(n + m)
def merge(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

Finding a common element in two sorted lists uses the same moves: equal → found; otherwise move the pointer at the smaller value.

### How to spot which pattern

| Clue in the problem | Pattern |
| --- | --- |
| sorted array + pair or sum | Opposite ends |
| palindrome, reverse in place | Opposite ends (swap, don't replace) |
| in place, remove, move, O(1) space | Slow and fast |
| two sorted arrays or lists | One pointer each |
| unsorted + pair sum | Not two pointers: use a dict |

## Your common mistakes and the checklist

Most of the marks you lost were habit mistakes, not gaps in understanding. Check every answer against this list before you send it.

| Mistake | Where it happened | Fix |
| --- | --- | --- |
| Code not run before sending | `x / 2`, `sortedb(b)`, `range(1, ...)` in move zeroes | Run 2–3 tests, including an edge case (empty, one element, already correct) |
| No complexity stated | count_evens, repeat, palindrome | Put `# Time: O(?) \| Space: O(?)` above every function |
| Multiplying steps that happen in sequence | count_evens, move_zeroes working | Add steps in sequence; multiply only nested ones |
| Counting a growing cost twice | repeat → said O(n³) | A growing cost is a sum; don't multiply it by n again |
| Space counted the input | count_evens → said O(n) | Count only the extra memory your code creates |
| Mixing up similar operations | replace vs insert; remove val vs remove duplicates | State the exact rule: what's compared, and which pointer moves |
| Imprecise explanations | why arr[i] is O(1); why Two Sum II skips | Explain the mechanism (the calculation, the smallest-value argument), not just the result |
| Missing indentation | most code answers | Write in your editor, then paste |

### Checklist, every solution

- Inside a `def`, properly indented
- 2–3 tests run, output pasted (one edge case)
- `# Time | Space` written above the function
- Explained in one precise sentence *why* it works

## Resources

Practice questions and LeetCode problems for this topic are in [practice_questions.md](practice_questions.md).

- [Python Wiki: TimeComplexity](https://wiki.python.org/moin/TimeComplexity): the official cost of every list, dict and set operation
- [Python string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [LeetCode Explore: Array and String](https://leetcode.com/explore/learn/card/array-and-string/): read the text and skip the C++ code (C++ `vector` = Python list)
- [NeetCode Roadmap](https://neetcode.io/roadmap): Arrays & Hashing, Two Pointers
- [Python Tutor](https://pythontutor.com/python-compiler.html): step through code and watch the pointers move
