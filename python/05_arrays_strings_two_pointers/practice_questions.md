# DSA Questions: Arrays, Strings & Two Pointers

Revise the matching notes doc first, then answer these without looking.

## Checklist for every answer

- [ ] Inside a `def`, properly indented (write it in your editor)
- [ ] 2–3 tests run, output pasted, including one edge case (empty, one element, already correct)
- [ ] `# Time | Space` written above the function
- [ ] One precise sentence on *why* it works

## Session questions

These are all the questions from our lessons, in the order we did them, with the original code and tests. Questions marked ★ are ones you lost marks on, so give them extra attention.

### Lesson 1: Arrays

**Q1 ★** Why is `arr[500]` just as fast as `arr[0]`? Explain the calculation the computer does.

**Q2** Which is faster on a list of 1 million items, and why?

- (a) `arr.pop()`
- (b) `arr.pop(0)`

**Q3** What is the time complexity of this code? Show your working and finish with the Big O.

```python
for x in arr:
    if x in arr:
        print(x)
```

**Q4 ★** Write `count_evens(arr)`, which returns how many even numbers are in the list. Give its time and space complexity.

```text
count_evens([1, 2, 3, 4])  → 2
count_evens([])            → 0
count_evens([7, 9])        → 0
```

**Q5 ★** You need to add 1,000 items to the **front** of a list, one at a time. Why is that slow (give the exact cost), and what could you do instead? Give two options with their Big O.

### Lesson 2: Strings

**Q1 ★** Why does `s[0] = "j"` give an error in Python, and what does Python do instead when you "change" a string? What's the difference between replacing and inserting?

**Q2 ★** What's the time complexity of this, and why? Show it as a sum.

```python
def repeat(s):
    result = ""
    for ch in s:
        result += ch + ch
    return result
```

Then rewrite it to be O(n) and give its time and space. `repeat("abc")` should return `"aabbcc"`.

**Q3 ★** Write `is_anagram(a, b)`, which returns `True` if the two strings use exactly the same letters the same number of times. Give its time and space complexity.

```text
is_anagram("listen", "silent")  → True
is_anagram("rat", "car")        → False
is_anagram("aab", "abb")        → False
```

**Follow-up:** the sorting solution is O(n log n). Write an O(n) version using a dict to count characters. Why is the length check needed for correctness?

**Q4 ★** `s[::-1] == s` checks whether a string is a palindrome in one line.

1. What are its time and space complexity?
2. Write a version that uses **O(1)** extra space, inside a `def`, with its complexity.

### Lesson 3: Two Pointers

**Warm-up** What is the difference between Two Sum (#1) and Two Sum II (#167)? Solve Two Sum #1 (unsorted) in O(n) time.

**Q1 ★** In Two Sum II, when `total > target` we move `right` left. Why can we safely skip every pair that uses the current `right`, without checking them? Give the precise argument.

**Q2 ★** Which pattern would you use for each of these? Give the pattern name **and the exact rule for moving the pointers**.

- (a) Reverse a list in place
- (b) Check whether two sorted lists have any element in common
- (c) Remove all occurrences of `val` from a list in place

**Q3 ★** Write `move_zeroes(nums)`, which moves all 0s to the end **in place** and keeps the order of the other numbers.

```text
[0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
[0]              → [0]
[1, 2]           → [1, 2]
```

**Q4 ★** Why does Two Sum II's two-pointer trick **fail** on an unsorted array? Give a small example where it gives the wrong answer and trace it step by step.

## Extra questions (new)

1. Write `reverse_list(nums)`, which reverses a list in place with two pointers. Give time and space.
2. Write `has_common(a, b)` for two sorted lists. Test it on `[1, 5]` and `[5, 9]`.
3. Write `remove_duplicates(nums)` for a sorted list, return the count of unique elements, and trace it by hand on `[1, 1, 2, 3, 3]`.
4. Write `remove_element(nums, val)` in place and test it on `[3, 2, 2, 3]` with `val = 3` (should keep 2 elements).

## LeetCode problems

Solve these in Python3, in this order, and tick each one when it's Accepted.

- [ ] [Reverse String](https://leetcode.com/problems/reverse-string/): opposite ends, swap
- [ ] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/): opposite ends, skip characters that fail `.isalnum()`
- [ ] [Move Zeroes](https://leetcode.com/problems/move-zeroes/): slow and fast
- [ ] [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/): opposite ends, 1-based answer
- [ ] [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/): one pointer each, fill from the back
- [ ] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/): stretch goal
