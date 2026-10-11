# Big O Notation: Practice Questions

For each code question, give the time and space complexity and one line of reasoning. Solve on paper first, then send your answers to Claude for grading.

## Session questions (already practiced)

These are the five self-check questions we worked through together. Redo them from scratch without looking at your notes. You should now get every one fully right, including the reasoning.

**S1.** What's the time complexity? other_list has length m.

```python
for i in range(n):
    if arr[i] in other_list:
        count += 1
```

**S2.** What's the time complexity? Trace it with n = 100 and list every value of i.

```python
i = 1
while i < n:
    i *= 3
```

**S3.** What's the time and space complexity?

```python
def reverse(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
```

Then rewrite it in O(n) time.

**S4.** Simplify O(3n² + 5n log n + 1000). Name both rules you used.

**S5.** The constraints say n ≤ 10⁵. Is an O(n²) solution OK? Show the arithmetic, then say which complexity you should aim for.

## Level 1: Simplify

Simplify each to its Big O form.

1. O(5n + 20)
2. O(n² + 100n + 7)
3. O(n log n + n)
4. O(3 × 2ⁿ + n³)
5. O(n + m), where m and n are sizes of two different arrays. Can you drop either term?
6. O(log₂ n + log₁₀ n)
7. Rank from fastest to slowest: O(n²), O(1), O(n log n), O(2ⁿ), O(log n), O(n), O(√n)

## Level 2: Loops

Use the k-steps method where it helps: write what i equals after k steps, set it equal to the stop condition, solve for k.

**Q8.**

```python
for i in range(n):
    print(i)
for j in range(n):
    print(j)
```

**Q9.**

```python
for i in range(n):
    for j in range(n):
        for k in range(10):
            print(i, j, k)
```

**Q10.**

```python
i = n
while i > 0:
    i //= 2
```

**Q11.** Trace this with n = 50 and list every value of i. Then give the complexity.

```python
i = 1
while i < n:
    i *= 2
```

**Q12.**

```python
for i in range(n):
    j = 1
    while j < n:
        j *= 2
```

**Q13.**

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

**Q14.**

```python
i = 1
while i * i <= n:
    i += 1
```

**Q15.** a has length m, b has length n.

```python
for x in a:
    for y in b:
        if x == y:
            print(x)
```

**Q16.**

```python
for i in range(0, n, 5):
    print(i)
```

## Level 3: Hidden costs in Python

Each of these looks like one loop. Check every line for hidden work.

**Q17.**

```python
def has_duplicate(nums):
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:]:
            return True
    return False
```

**Q18.**

```python
def has_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

**Q19.**

```python
queue = list(range(n))
while queue:
    item = queue.pop(0)
```

**Q20.**

```python
words = []
for i in range(n):
    words.append(str(i))
result = ",".join(words)
```

**Q21.**

```python
for i in range(n):
    total = sum(nums)
    print(total + i)
```

How would you rewrite it to be O(n)?

**Q22.**

```python
nums.sort()
for x in nums:
    print(x)
```

**Q23.**

```python
def is_palindrome(s):
    return s == s[::-1]
```

## Level 4: Space and recursion

Give both time and space. Remember that each waiting recursive call uses stack space.

**Q24.**

```python
def count_down(n):
    if n == 0:
        return
    count_down(n - 1)
```

**Q25.**

```python
def halve(n):
    if n <= 1:
        return
    halve(n // 2)
```

**Q26.**

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Draw the call tree for fib(5). How many calls are there?

**Q27.**

```python
def make_grid(n):
    return [[0] * n for _ in range(n)]
```

**Q28.**

```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

**Q29.**

```python
def reversed_copy(arr):
    return arr[::-1]
```

Compare Q28 and Q29. Which uses less extra space, and why?

## Level 5: Constraints and optimizing

Show the arithmetic. Use about 10⁸ operations per second.

**Q30.** n ≤ 2,000. Is an O(n²) solution OK? What about O(n³)?

**Q31.** n ≤ 10⁶. Which of these fit: O(n²), O(n log n), O(n)?

**Q32.** n ≤ 20. The problem asks you to check every subset. Is O(2ⁿ) OK?

**Q33.** Give the complexity of this brute-force Two Sum, then describe (in words or code) a faster approach and its time and space.

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

**Q34.** Find the bottleneck and the total complexity. How would you fix it?

```python
def common_items(a, b):
    a.sort()
    result = []
    for x in a:
        if x in b:
            result.append(x)
    return result
```

**Q35.** A web page loads a list of n users, then runs one database query per user to get their profile. Each query takes about 5 ms. What's the shape of this problem, and how long does it take for n = 2,000? How would you fix it?
