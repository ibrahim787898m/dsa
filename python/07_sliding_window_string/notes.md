# Sliding Window & Strings — Concept Notes

## 1. Fixed-size sliding window

When the window length `k` is given, slide it one step at a time: add the element entering on the right and remove the one leaving on the left. That turns O(n·k) brute force into O(n) time and O(1) space.

**Why brute force is slow:** neighbouring windows overlap in k−1 elements, and brute force re-adds them every time. When k ≈ n/2, O(n·k) becomes O(n²).

```python
def max_sum(nums, k):
    window = sum(nums[:k])          # build the first window
    best = window
    for right in range(k, len(nums)):
        window += nums[right]       # element entering
        window -= nums[right - k]   # element leaving
        best = max(best, window)
    return best
```

**Why the element leaving is `nums[right - k]`:** before adding, the window covers indices `right-k` … `right-1` (k elements). After adding `nums[right]` there are k+1 elements, so the oldest one, `right - k`, must go. Using `right - k + 1` removes the wrong element and the window stops being contiguous (an off-by-one error).

**Max average (LC 643):** track the max sum, then divide by k once at the end. All windows have the same size, so the biggest sum is also the biggest average. On LeetCode, pick **Python3**: in Python 2, `int / int` does integer division.

**How to recognize it:** "contiguous subarray/substring" plus a **given length k**.

## 2. Variable-size sliding window

When the problem gives a **condition** instead of a length, the window grows with `right` every step and shrinks with `left` only when needed. The loop is: grow, shrink **while** needed, then record.

```python
def longest_at_most(nums, limit):       # longest subarray with sum <= limit
    left = window = best = 0
    for right in range(len(nums)):
        window += nums[right]              # 1. grow
        while window > limit:              # 2. shrink WHILE invalid
            window -= nums[left]
            left += 1
        best = max(best, right - left + 1) # 3. record (window is valid)
    return best
```

| Goal | Shrink while... | Record the answer... | Start `best` at |
| --- | --- | --- | --- |
| Longest window | the window is **invalid** | **after** the while loop | 0 |
| Shortest window (LC 209) | the window is **valid** | **inside** the while loop, before shrinking | `float("inf")` |

**Why it is O(n), not O(n²):** each pass of the while loop moves `left` forward by 1. `left` starts at 0, never moves back, and can't pass n, so the while loop runs **at most n times in total** across the whole run. Total work ≤ 2n. Counting total work across the run like this is called **amortized analysis**.

**Window length = `right - left + 1`:** `right - left` counts the gaps between the indices, but the window includes **both** endpoints (inclusive). Edge case: one element means `left == right`, so `right - left = 0` would be wrong.

**Limitation:** the sum version needs **all positive numbers**. With negatives, adding an element can make the sum smaller, so shrinking early throws away windows that could have become valid. Example: `[3, 8, -2]`, limit 7 → the algorithm returns 1, but `[8, -2] = 6` gives 2. Use prefix sums or Kadane's algorithm instead.

**Counting instead of summing (LC 1004):** the "longest window with at most k zeros" uses the same template with a `zeros` counter in place of the sum.

**How to recognize it:** longest / shortest / min / max **contiguous** subarray such that [condition], with no fixed length.

## 3. Python strings essentials

**Strings are immutable, lists are mutable.** Most string performance rules follow from that one line.

- **No in-place edits:** `s[0] = "S"` raises `TypeError`. Build a new string (`"S" + s[1:]`) or convert with `list(s)`, edit, then `"".join(...)`.
- **`+=` in a loop can be O(n²):** each `+=` creates a new string and copies every old character, so the copies cost 1 + 2 + … + n = n(n+1)/2. The fix is to `append` to a list (O(1) each), then `"".join(parts)` once (O(n)).
- **Slicing copies:** `s[i:j]` costs O(j − i). The end is **exclusive**, so its length is `j - i` (e.g. `"sliding"[2:5]` = `"idi"`). `s[::-1]` reverses.
- **Character tools:** `isalpha()`, `isdigit()`, `isalnum()`, `lower()`, `upper()`.
- **`ord` / `chr`:** `ord("a")` = 97, `chr(97)` = `"a"`. Letters a–z are consecutive, so `ord(c) - ord("a")` maps them to 0–25, i.e. list indices.

**Counting characters, three ways:**

| Approach | Time | Space | Use when |
| --- | --- | --- | --- |
| `sorted(s) == sorted(t)` | O(n log n) | O(n) | Quick to write, slowest |
| `dict` / `Counter` | O(n) | O(k) distinct chars | Any characters, including Unicode |
| `[0] * 26` + `ord` | O(n) | O(1) | Lowercase a–z only, fastest |

`collections` is part of Python's **standard library**. Importing it doesn't make code slower.

**Anagram with one array (LC 242):** check that the lengths are equal, add counts for `s`, subtract for `t`, and return False the moment a count goes negative. With equal lengths, no negative count means every count is 0.

**Two pointers on strings (LC 125, O(1) space):** skip junk in place instead of building a cleaned copy.

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

The inner loops need `left < right` too, or input like `".,"` runs out of bounds.

## 4. Sliding window on strings

Most string window problems combine a window (sections 1–2) with character counting (section 3).

**Pattern A: variable window + hash map (LC 3, Longest Substring Without Repeating Characters)**

```python
def length_of_longest_substring(s):
    seen = {}                               # char -> count in window
    left = best = 0
    for right in range(len(s)):
        c = s[right]
        seen[c] = seen.get(c, 0) + 1        # grow
        while seen[c] > 1:                  # shrink while invalid
            seen[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)  # record
    return best
# "abcabcbb" -> 3, "pwwkew" -> 3
```

**Why checking only `seen[c]` is enough (an invariant):** at the end of every step, the window has no duplicates. The next step adds just one character, `c`, so `c` is the only one whose count changed and the only one that can be duplicated.

**Pattern B: fixed window + count array (LC 438, Find All Anagrams)**

```python
def find_anagrams(s, p):
    k = len(p)
    if k > len(s):
        return []
    need, window = [0] * 26, [0] * 26
    for c in p:
        need[ord(c) - ord("a")] += 1
    result = []
    for right in range(len(s)):
        window[ord(s[right]) - ord("a")] += 1          # enters
        if right >= k:
            window[ord(s[right - k]) - ord("a")] -= 1  # leaves
        if window == need:
            result.append(right - k + 1)               # window start
    return result
# find_anagrams("cbaebabacd", "abc") -> [0, 6]
```

This fixed-window style has no separate first-window step: `if right >= k` means nothing leaves until the window is full.

## 5. Which pattern to use

| The problem says... | Pattern | Example |
| --- | --- | --- |
| subarray/substring of **length k** | Fixed window | LC 643, LC 1456 |
| anagram / permutation of a pattern | Fixed window + count array | LC 438, LC 567 |
| **longest** ... such that [condition] | Variable: shrink while invalid, record after | LC 3, LC 1004, LC 424 |
| **shortest / minimum** ... such that [condition] | Variable: shrink while valid, record inside | LC 209, LC 76 |
| sum condition with **negative numbers** | Not sliding window: prefix sums / Kadane | later topic |

For conditions on characters (no repeats, at most k distinct), track them with a dict or a 26-slot array.

## 6. Complexity cheat sheet

| Operation | Cost |
| --- | --- |
| `s[i]`, `len(s)` | O(1) |
| `s[i:j]` | O(j − i), it copies |
| `s == t`, `c in s` | O(n) |
| `"".join(parts)` | O(n) |
| `+=` on a string in a loop | O(n²) worst case |
| `sorted(x)`, `x.sort()` | O(n log n) |
| `Counter(x)`, `set(x)`, building a dict | O(n) |
| `x in list` | O(n) |
| `x in set`, `x in dict` | O(1) average |
| `min`, `max`, `sum` | O(n) |
| `list.append(x)`, `list.pop()` | O(1) |
| `list.insert(0, x)`, `list.pop(0)` | O(n), shifts everything |

When comparing two approaches, ask what each one does to every element, not whether it is built-in or imported.

## 7. My common mistakes

1. **Stopping the while loop after one shrink.** After every shrink, write the check: `8 > 7? ✗ shrink again`. Fixed by Lesson 4 Q2. Keep doing it.
2. **Off-by-one on ranges.** A window is inclusive (`right - left + 1`), a slice is exclusive (`s[i:j]` has length `j - i`).
3. **Proving with one example instead of the general rule.** When asked "why," state the rule or invariant, then use an edge case as proof.
4. **Not reading constraints fully** (e.g. "O(1) extra space"). The constraint is often the point of the question.
5. **Logic bugs that look like typos** (a missing `not`, `.lower` without `()`). Run the code, or trace a tiny input that should fail, like `"ab"`.
6. **Wrong starting value:** `best = 0` or `inf` for a max, `float("inf")` for a min.
7. **Mixing up `>` and `>=`** in the while condition.
