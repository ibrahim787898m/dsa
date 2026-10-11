# Binary Search — Concept Notes

## 1. The idea

Binary search finds a target in a **sorted** array by checking the middle element and throwing away the half that can't contain the target. Each check halves the search space, so it runs in O(log n) time.

**The three cases at `mid`:**

- `nums[mid] == target` → found
- `nums[mid] < target` → target is to the right, discard the left half
- `nums[mid] > target` → target is to the left, discard the right half

**Worked example:** `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`, target 23

| Step | Range | mid | nums[mid] | Decision |
| --- | --- | --- | --- | --- |
| 1 | 0–9 | 4 | 16 | 16 < 23 → go right |
| 2 | 5–9 | 7 | 56 | 56 > 23 → go left |
| 3 | 5–6 | 5 | 23 | Found |

### Why O(log n)

The range shrinks n → n/2 → n/4 → … → 1. The number of halvings is log₂(n).

| n | Linear (worst) | Binary (worst) |
| --- | --- | --- |
| 1,000 | 1,000 | ~10 |
| 1,000,000 | 1,000,000 | ~20 |
| 1,000,000,000 | 1,000,000,000 | ~30 |
| 1,000,000,000,000 | 1,000,000,000,000 | ~40 |

**Shortcut:** 2¹⁰ = 1,024 ≈ 1,000, so every 3 zeros ≈ 10 halvings.

### Log base: math class vs CS

- In school math, `log` usually means log₁₀. In CS, `log` means **log₂**, because algorithms halve.
- For **Big O**, the base doesn't matter: bases differ by a constant factor, and Big O drops constants.
- For **counting actual steps**, use base 2. Mistake to avoid: log₁₀(10⁹) = 9, but binary search on a billion items takes about 30 steps.

### The requirement: monotonic order

Binary search only works if one comparison tells you for certain which half to discard. A sorted array (always increasing or always decreasing) guarantees this.

- On an unsorted array like `[7, 2, 9, 4, 1]`, searching for 4 discards the half that contains it and returns "not found".
- Sorting first costs O(n log n). For a **single** search that's worse than linear search at O(n). Sort only when you'll search the same array **many times**.
- Sorting loses the original indexes. If you need them, sort `(value, index)` pairs.
- Descending order works too, but the comparisons flip.

**Link to two pointers:** `low` and `high` are two pointers moving toward each other, but they jump by half the range instead of one step.

## 2. The standard template

Memorize this iterative version. It's O(log n) time and O(1) space.

```python
def binary_search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid            # found
        elif nums[mid] < target:
            low = mid + 1         # target is to the right
        else:
            high = mid - 1        # target is to the left

    return -1                     # range is empty, not found
```

### Why each detail matters

| Detail | Why | What breaks otherwise |
| --- | --- | --- |
| `high = len(nums) - 1` | `high` is the last valid index; the range `[low, high]` includes both ends | Index out of range |
| `while low <= high` | When `low == high`, one element is still unchecked | `[5]`, target 5 → loop never runs, returns -1 |
| `low = mid + 1`, `high = mid - 1` | `mid` was already checked, so exclude it; every step must **shrink** the range | `low = mid` can loop forever |
| `return -1` after the loop | Loop ends when `low > high`, meaning the range is empty | |

### Trace: target not in the array

`[1, 4, 6, 9, 13]`, target 7

| Step | low | high | mid | nums[mid] | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 4 | 2 | 6 | 6 < 7 → low = 3 |
| 2 | 3 | 4 | 3 | 9 | 9 > 7 → high = 2 |
| 3 | 3 | 2 | | | low > high → return -1 |

When the search fails, `low` ends at the index where the target **would be inserted** (here 3). Section 3 uses this.

**Tracing habit:** write every pointer update, including the last one. The loop ends on the *next* check after `high` or `low` moves, not at the comparison itself.

### The infinite loop with `low = mid`

If the range shrinks to two adjacent indexes (`high = low + 1`), then `(low + high) // 2` rounds down to `low`. With `low = mid`, nothing changes and the loop never ends. It happens with any array length:

- `[1, 3]`, target 5 → low 0, high 1, mid 0, low = 0, forever
- `[1]`, target 5 → low = high = mid = 0, forever

**Debugging question:** can `mid` ever equal `low` (or `high`) without the range shrinking?

### Overflow note (C, Java)

In C and Java, `low + high` can overflow for huge indexes, so use `mid = low + (high - low) // 2`. Python integers don't overflow, so `(low + high) // 2` is fine there.

### Recursive version

```python
def binary_search(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, high)
    else:
        return binary_search(nums, target, low, mid - 1)
```

The recursive version uses O(log n) stack space. Prefer the iterative version.

## 3. Variants: first, last, count, insert position

When the array has duplicates or the target is missing, don't stop at the first match: **save the index and keep searching** in the direction you care about.

### First occurrence (leftmost)

```python
def first_occurrence(nums, target):
    low, high = 0, len(nums) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            result = mid          # save candidate
            high = mid - 1        # keep looking LEFT
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
```

### Last occurrence (rightmost)

Same code, one line changed in the match branch:

```python
        if nums[mid] == target:
            result = mid
            low = mid + 1         # keep looking RIGHT
```

Trace of first occurrence of 3 in `[1, 3, 3, 3, 5, 8]`:

| Step | low | high | mid | nums[mid] | Action | result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 5 | 2 | 3 | match → save, go left | 2 |
| 2 | 0 | 1 | 0 | 1 | 1 < 3 → low = 1 | 2 |
| 3 | 1 | 1 | 1 | 3 | match → save, go left | 1 |
| 4 | 1 | 0 | | | loop ends | **1** |

### Count occurrences in O(log n)

Count = last − first + 1, but **check for "not found" first**. Otherwise both return -1 and you get −1 − (−1) + 1 = 1 instead of 0.

```python
first = first_occurrence(nums, target)
if first == -1:
    return 0
return last_occurrence(nums, target) - first + 1
```

Store `first` in a variable rather than calling the function twice.

### Insert position (lower bound)

The standard template with one change: return `low` instead of `-1`.

```python
def search_insert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
```

**Why it works:** throughout the search, everything left of `low` is < target and everything right of `high` is > target. When the loop ends with `low = high + 1`, `low` is the first index with a bigger value.

**Edge cases** with `[1, 3, 5, 6]`:

- Target smaller than everything (0) → returns **0**; `low` never moves
- Target bigger than everything (7) → returns **len(nums) = 4**, meaning append at the end; `high` stays at 3 while `low` moves up
- Target in a gap (4) → returns 2

### Avoid the linear trap

Finding any match and then walking left one step at a time is O(n) in the worst case (an array of a million 3s). Always use a second binary search instead. Every variant here stays O(log n) time and O(1) space.

## 4. Advanced patterns

The general rule: **binary search works whenever one check lets you throw away half the possibilities.** The data doesn't have to be a plain sorted array.

### A. Search in a rotated sorted array (LeetCode 33)

`[4, 5, 6, 7, 0, 1, 2]` is a sorted array rotated at some point. Key fact: **when you split at `mid`, at least one half is fully sorted.**

1. Find the sorted half: `nums[low] <= nums[mid]` → left half sorted; otherwise right half sorted.
2. If the target lies inside the sorted half's range, search there. Otherwise search the other half.

```python
def search_rotated(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:                 # left half sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:                                      # right half sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
```

Trace on `[6, 7, 8, 1, 2, 3, 4, 5]`, target 2:

| Step | low | high | mid | nums[mid] | Sorted half | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 7 | 3 | 1 | nums[0]=6 > 1 → right | 1 < 2 ≤ 5 → low = 4 |
| 2 | 4 | 7 | 5 | 3 | nums[4]=2 ≤ 3 → left | 2 ≤ 2 < 3 → high = 4 |
| 3 | 4 | 4 | 4 | 2 | | found → 4 |

**Trace the code as written:** compare with `nums[low]`, not `nums[0]`. Comparing with `nums[0]` is a valid variant, but a trace should follow the actual code so it can catch bugs in it. Always state which half is sorted at each step.

### B. Binary search on the answer

Sometimes there's no array to search. You search a **range of possible answers** instead.

**How to spot it:**

1. The question asks for a **minimum or maximum** value.
2. You can write a yes/no check `is_valid(k)`.
3. The answers are **monotonic**: if `k` works, every bigger `k` works (or every smaller one).

Then the check results look like ❌ ❌ ❌ ✅ ✅ ✅ (or the reverse), and you search for the first ✅ or the last ✅, using the first/last occurrence patterns from section 3.

**Example 1: integer square root (LeetCode 69).** Find the largest `k` with `k * k <= x`. This is a "last ✅" search:

```python
def my_sqrt(x):
    low, high = 0, x          # optional: high = x // 2 for x >= 2
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= x:
            ans = mid          # valid, save it
            low = mid + 1      # try bigger
        else:
            high = mid - 1
    return ans
```

Tests: `my_sqrt(0) = 0`, `my_sqrt(1) = 1`, `my_sqrt(8) = 2`, `my_sqrt(16) = 4`.

**Example 2: Koko Eating Bananas (LeetCode 875).** Find the slowest speed `k` that lets Koko finish all piles within `h` hours. This is a "first ✅" search.

- **Range:** `low = 1` (speed 0 never finishes), `high = max(piles)`. She eats from one pile per hour, so any speed above the largest pile wastes time. And since `h` can be as small as `len(piles)`, the largest pile may need to go in one hour.
- **Check `can_finish(k)`:** total hours = sum of ⌈pile / k⌉ over all piles; return `total <= h`. Round up, because she doesn't start the next pile within the same hour.
- **Round up in Python:** `math.ceil(pile / k)` or `(pile + k - 1) // k`.

Worked check with `piles = [3, 6, 7, 11]`, `h = 8`:

| Speed k | Hours per pile | Total | ≤ 8? |
| --- | --- | --- | --- |
| 3 | 1, 2, 3, 4 | 10 | No |
| 4 | 1, 2, 2, 3 | 8 | Yes ← answer |
| 5 | 1, 2, 2, 3 | 8 | Yes |
| 11 | 1, 1, 1, 1 | 4 | Yes |

**Complexity:** O(log(range) × cost of check). `my_sqrt` is O(log x). Koko is O(n × log(max pile)), because each check loops over all n piles.

## 5. Bugs, testing and cheat sheet

### Common bugs

| Bug | Symptom | Fix |
| --- | --- | --- |
| `while low < high` with the standard template | Misses the last element (`[5]`, target 5 → -1) | `while low <= high` |
| `low = mid` or `high = mid` | Infinite loop when the range is 1–2 elements | `mid + 1` / `mid - 1` |
| `high = len(nums)` | Index out of range | `len(nums) - 1` |
| `len(nums - 1)` | `TypeError` (list minus int) | `len(nums) - 1` |
| Count without a not-found check | Returns 1 for a missing target | Return 0 if first == -1 |
| Walking linearly after a match | O(n) on many duplicates | Second binary search |
| Running on unsorted data | Wrong "not found" | Sort first, or use another approach |

### Testing checklist

Run every binary search on at least these cases, and paste the actual output:

- [ ] Target at the first index
- [ ] Target at the last index
- [ ] Target in the middle
- [ ] Target **not found** (smaller than all, bigger than all, in a gap)
- [ ] **Empty** array
- [ ] Single-element array (found and not found)
- [ ] Duplicates (for first/last/count)

### Complexity cheat sheet

| Algorithm | Time | Space |
| --- | --- | --- |
| Linear search | O(n) | O(1) |
| Binary search (iterative) | O(log n) | O(1) |
| Binary search (recursive) | O(log n) | O(log n) |
| First / last occurrence, count, insert position | O(log n) | O(1) |
| Sort + one search | O(n log n) | depends on sort |
| Rotated sorted array search | O(log n) | O(1) |
| Binary search on answer | O(log(range) × check) | O(1) |

### Which template?

| Question asks for | Use |
| --- | --- |
| Is the target there / its index | Standard template |
| Leftmost match, or the smallest valid answer | First occurrence (save, go left) |
| Rightmost match, or the largest valid answer | Last occurrence (save, go right) |
| Where it would go | Standard template, return `low` |
| Array is rotated | Find the sorted half first |
