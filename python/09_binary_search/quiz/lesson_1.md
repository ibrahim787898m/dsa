# Binary Search — Quiz 1

## Q1

**Array: [3, 9, 14, 20, 27, 31, 40, 48], target = 31. Write out each step the way the walkthrough table does: range, mid, value, decision. Use mid = (low + high) // 2.**

```text
step 1 -> range 0 - 7 -> mid 3 -> num 20 -> 20 < 31 -> through left
step 2 -> range 4 - 7 -> mid 5 -> num 31 -> found
```

## Q2

**Running binary search on [7, 2, 9, 4, 1] to find 4 might fail. Why? What would you have to do first, and what would that cost in Big O?**

because the array is not sorted and it is not either always increasing or always decreasing order, you can see 2 is in between to large number 7 and 9, so when we do the binary search we will miss the target. to apply the binary search obviously we need to sort the array first in any order and if we use sorted function it will cost nlogn time complexity.

## Q3

**An array has about 1,000,000,000 elements. Roughly how many comparisons does binary search need in the worst case? Explain how you got your answer.**

30

```text
log2(1000000000) = x
or
9 ÷ 3 × 10 = 30.
or
2¹⁰ ≈ 1 thousand (10³)
2²⁰ ≈ 1 million (10⁶)
2³⁰ ≈ 1 billion (10⁹)
```
