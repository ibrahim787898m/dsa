# Sliding Window — Quiz: Lesson 4

## Q1

**In `length_of_longest_substring`, the while loop only checks `seen[c] > 1` for the new character c, not every character in the window. Why is that enough?**

when single char count goes above 1 it means this char is repeating so we this condition we can shrink the window dont need to check each chars

## Q2 (trace)

**Trace `length_of_longest_substring("pwwkew")`. Show every shrink pass separately (with the ✓/✗ check), and give the final answer.**

```text
right=0 'p': window "p"      len 1  best 1
right=1 'w': window "pw"     len 2  best 2
right=2 'w': w=2 -> remove 'p' left=1 -> w=2 ✗ window "ww" best 2
        -> remove 'w' left=2 -> w=1 ✓ window "w" best 2
right=3 'k': window "wk"     len 2 best 2
right=4 'e': window "wke"    len 3 best 3
right=5 'w': w=2 -> remove 'w' left=3 -> w=1 ✓ window "kew" best 3

answer = 3
```

## Q3

**In `find_anagrams`, the line `window == need` compares two lists of 26 items on every step. What's the total time complexity, and why is it still considered O(n)? What would you change if the strings could contain any character, not just a–z?**

```python
def find_anagrams(s, p):
    k = len(p)
    if k > len(s):
        return []

    need = [0] * 26
    window = [0] * 26
    for c in p:
        need[ord(c) - ord("a")] += 1

    result = []
    for right in range(len(s)):
        window[ord(s[right]) - ord("a")] += 1          # char enters
        if right >= k:
            window[ord(s[right - k]) - ord("a")] -= 1  # char leaves
        if window == need:
            result.append(right - k + 1)               # window start
    return result
# find_anagrams("cbaebabacd", "abc") → [0, 6]
```

## Q4

**Name the pattern for each problem (fixed, variable-longest, or variable-shortest), with a one-line reason:**

- a) LC 567: does s2 contain a permutation of s1?
- b) LC 76: the smallest substring of s containing all characters of t
- c) LC 1456: max vowels in any substring of length k
- d) LC 424: the longest substring you can make all one letter by replacing at most k characters

## Q5 (code)

**LeetCode 567, Permutation in String: return True if s2 contains a permutation of s1 as a substring.**

```text
s1 = "ab", s2 = "eidbaooo" → True   ("ba" is in s2)
s1 = "ab", s2 = "eidboaoo" → False
```
