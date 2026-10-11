# Sliding Window — Quiz: Lesson 3

## Q1

**Why can building a string with `+=` in a loop be O(n²)? What's the fix, and why is the fix O(n)? (Try using the words copy and immutable.)**

```python
result = ""
for c in s:
    result += c
```

when we are using += in a for loop each time we copy the previous created string like in first loop copied string 0 -> added a char, 2nd loop carried 1 added 1, 3rd loop carried 2, 4th loop carried 3 so like that it is 1 + 2 + 3 + 5 + 6 ... + n which is like n(n + 1) / 2 -> O(n^2). so instead of doing this we create an empty array and copy each char in the array which is 1 times per loop and then join each char to create the string which is n times so the complexity is O(n)

## Q2

**What does each line print, or does it raise an error?**

```python
s = "sliding"
print(s[2:5])
print(s[::-1])
print(ord("e") - ord("a"))
s[0] = "S"
```

```text
s = "sliding"
print(s[2:5]) -> idin
print(s[::-1]) -> gnidils
print(ord("e") - ord("a")) -> 101 - 97 = 4
s[0] = "S" -> error
```

## Q3

**Two anagram checks:**

```python
def a(s, t): return sorted(s) == sorted(t)
def b(s, t): return Counter(s) == Counter(t)
```

**Give the time complexity of each and say which one is faster for long strings, and why.**

these are built in python function i know. sorted is faster, to use counter function we need to include the external library.

## Q4 (code)

**LeetCode 242, Valid Anagram. Write `is_anagram(s, t)` using a 26-length count array, not sorted or Counter. Return True if t is an anagram of s. Hint: you only need one array. Add for s, subtract for t.**

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            count[ord(char) - ord("a")] += 1

        for char in t:
            count[ord(char) - ord("a")] -= 1
            if count[ord(char) - ord("a")] < 0:
                return False
        return True
```

## Q5 (code)

**LeetCode 125, Valid Palindrome. A phrase is a palindrome if, after lowercasing and ignoring non-alphanumeric characters, it reads the same forward and backward.**

```text
"A man, a plan, a canal: Panama" → True
"race a car" → False
```

**Solve it with two pointers and O(1) extra space. Don't build a cleaned copy of the string. Skip the characters in place instead.**

### First attempt

```python
def isPalindrome(self, s) -> bool:
    s = ''.join(ch for ch in s if ch.isalnum())
    s = s.lower

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
```

### Second attempt

```python
def isPalindrome(self, s) -> bool:

    left = 0
    right = len(s) - 1

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
