# Strings — Quiz: Lesson 2

## Q1

**Why does `s[0] = "j"` give an error in Python, and what does Python do instead when you "change" a string?**

when i try to do s[0]  = "j" maybe it try to replace the 0th char of the string but as it is immutable it gives me error or maybe it is not a dynamic array thats why we cant increase the length of the array thats why when we do s[0] = "j" it try to place the j in the 0th position and move the rest to right but it cant be done because we cant move the array from the location and increase the length as it is not dynamic array.

## Q2

**What's the time complexity of this, and why?**

```python
def repeat(s):
    result = ""
    for ch in s:
        result += ch + ch
    return result
```

**Then rewrite it to be O(n).**

```text
def repeat(s):
    result = "" O(1)
    for ch in s: O(1) * n times
        result += ch + ch O(1) here it is important the result is growing like 2, 4, 6, 8, ...n so it is n(n+2)/4 n^2
    return result O(1)
T = O(1) + (n * n^2 * O(1)) + O(1)
= n^3
= O(n^3)
```

```python
def repeat(s):
    parts= []
    for ch in s:
        parts.append(ch + ch)
    result = "".join(parts)
    return result
```

## Q3

**Write `is_anagram(a, b)`, which returns True if the two strings use exactly the same letters the same number of times ("listen", "silent" → True). Give its time and space complexity. Test it on 2–3 inputs before you send it.**

```python
def is_anagram(a, b):
    if len(a) != len(b):
        return False
    return sorted(a) == sortedb(b)
```

```python
def is_anagram(a, b):
    if len(a) != len(b):
        return False

    count = {}

    for char in a:
        count[char] = count.get(char, 0) + 1

    for char in b:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True
```

## Q4 (thinking question)

**`s[::-1] == s` checks whether a string is a palindrome in one line. What are its time and space complexity? Can you think of a way to check it using O(1) extra space? (This leads straight into Lesson 3.)**

the time complexity of this algorithm i mean the reversing string algorithm is O(k) for this case we are reversing the entire string so the input in n so the complexity is O(n) for time and O(n) for space.

if we do two pointer technique like

```python
left = 0
right = len(s) - 1

while left < right:
    if s[left].lower() != s[right].lower():
        return False
    left += 1
    right -= 1

return True
```
