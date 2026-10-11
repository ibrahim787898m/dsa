# Arrays — Quiz: Lesson 1

## Q1

**Why is `arr[500]` just as fast as `arr[0]`?**

for example.

```text
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
       0  1  2  3  4  5  6  7  8
```

so in computer memory these char stays in the specific location and computer knows it. so when we call for arr[0] computer immediately knows that in this position the char is 1 and when we call the arr[8] computer check the memory and knows that in this location the char is 9. it does not need to loop through the array to check which char is in which position. just it can tell from its memory.

## Q2

**Which is faster on a list of 1 million items, and why?**

- (a) `arr.pop()`
- (b) `arr.pop(0)`

arr.pop() means just remove a char from the end so computer can just locate the last char and remove it. dont need to move the array so the time is constant but when we do arr.pop(0) that means we are removing the 1st char of the array so we need to move the 2nd char to 1st 3rd char to 2nd 4th char to 3rd like that we need to do million times so time should be O(n) as the input grows the work also grows.

## Q3

**What is the time complexity of this code?**

```python
for x in arr:
    if x in arr:
        print(x)
```

```text
for x in arr: o(1) * n times
if x in arr: o(1) * n times
print(x) o(1)
T = n * O(1) * (n * O(1) + O(1)
= n * c1 * (n * c2 + c3)
= n * c1 * ( n * c4)
= n * n * c5
= n^2 c5
= n^2
O(n^2)
```

## Q4

**Write a function `count_evens(arr)` that returns how many even numbers are in the list. Give its time and space complexity.**

```text
def count_evens(arr):
    count = o O(1)
    for x in arr: O(1) n times
        if x / 2 == 0: O(1)
            count += 1 O(1)
    return count O(1)
T = O(1) + (n * O(1) * O(1) * O(1)) + O(1)
= O(n)
S = O(n)
```

## Q5 (thinking question)

**You need to add 1,000 items to the front of a list, one at a time. Why is that slow, and what could you do instead?**

it is slow because when we are adding each num at a time the list is moving from left to right and we are working 1000 times to add at the front each by each. we can do first create a list with these 1000 nums and then merge both list together to get O(1) time complexity
