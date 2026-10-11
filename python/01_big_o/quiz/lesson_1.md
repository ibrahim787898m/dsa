# Big O and Space — Quiz

## Q1

**What's the time complexity?**

```python
for i in range(n):
    if arr[i] in other_list:
        count += 1
```

```text
for i in range(n):   -> O(n) we are checking each element of n
   if arr[i] in other_list:   we are again checking each element of other_list with the arr[i] O(m) if the element is different if same as n it is O(n)
      count += 1 either O(m) or O(n) accordingly
```

so lets calculate

```text
O(n) * (O(m) + O(m))
O(n) * O(m + m)
O(n) * O(2m)
O(n) * O(m)
O(n * m)
```

if other_list is same as n

```text
O(n) * (O(n) + O(n))
O(n) * O(n + n)
O(n) * O(2n)
O(n) * O(n)
O(n * n)
```

## Q2

**What's the time complexity?**

```python
i = 1
while i < n:
    i *= 3
```

```text
i = 1 -> n(1)
while i < n:
i *= 3 -> n(1)
```

i dont undestand how to find logn mathematically i know it is logn time complexity because each time the i is getting bigger so the itter is getting smaller. like if the n is 100 then first itter i = 3 2nd itte i = 27 3rd itte i = 19683 so we wont get 4th itte and the code will end. so it is fast like logn time. but if the condition was like i = 1 while i < n: i += 1 and n = 100 so we need to do like 100 times so the time coplex will be n times.

## Q3

**What's the time and space complexity?**

```python
def reverse(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
```

isnt it O(n) because there are only one for loop

## Q4

**Simplify: O(3n² + 5n log n + 1000)**

4 is O(n*2) because other term time complexity is less than the n*2 one.

## Q5

**Constraints say n ≤ 10⁵. Is an O(n²) solution OK?**

n is so bigger in this case if we use the n^2 solution the time will take so much i guess . we should use a solution that will reduce time and we know it is logn so i guess O(logn) is the one we should choose.
