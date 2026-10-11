# Sliding Window & Strings — Practice Questions

## Unfinished Lesson 4 quiz questions

- [ ] **Q3.** In `find_anagrams`, `window == need` compares two 26-item lists on every step. What is the total time complexity, and why is it still called O(n)? What would you change if the strings could contain **any** character, not just a–z?
- [ ] **Q4.** Name the pattern (fixed, variable-longest, variable-shortest) with a one-line reason:
  - a) LC 567: does `s2` contain a permutation of `s1`?
  - b) LC 76: the smallest substring of `s` containing all characters of `t`
  - c) LC 1456: max vowels in any substring of length k
  - d) LC 424: the longest substring you can make all one letter by replacing at most k characters
- [ ] **Q5 (code).** LC 567, *Permutation in String*: return `True` if `s2` contains a permutation of `s1`. `s1 = "ab", s2 = "eidbaooo"` → True; `s1 = "ab", s2 = "eidboaoo"` → False. Run your code before submitting.

## Redo list: questions I scored low on

- [ ] **Lesson 3 Q3 (2/10).** Give the time complexity of `sorted(s) == sorted(t)` and of `Counter(s) == Counter(t)`. Which is faster for long strings, and why? Answer with Big O, not "built-in vs imported."
- [ ] **Lesson 4 Q1 (5/10).** In LC 3, why is it enough to check only `seen[c] > 1` for the new character? Use the word *invariant*.
- [ ] **Lesson 2 Q3 (7/10).** Why is window length `right - left + 1`? Give the general rule and an edge case, not one example.
- [ ] **Lesson 2 Q4 (8/10).** Build a small array with a negative number that breaks `longest_at_most`. Show the algorithm's answer, the correct answer, and a one-line *why*.
- [ ] **Bonus.** Write LC 125 (Valid Palindrome) with O(1) extra space from memory, then run it on `"ab"`, `".,"` and `"race a car"`.

## All lesson quiz questions

Every question from the session, to redo from scratch without looking at your old answers.

**Lesson 1: Fixed-size window**

- [ ] **Q1.** Give the time complexity of the brute force and of the sliding window version of max-sum-of-k. Explain *why* the sliding window version is faster.
- [ ] **Q2 (trace).** `max_sum([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], k=3)`: write the window sum after each slide and the final answer.
- [ ] **Q3.** Why is the element leaving `nums[right - k]` and not `nums[right - k + 1]`? Give the general rule, and show what breaks with the wrong one.
- [ ] **Q4.** Yes or no for a fixed window, with a reason: a) average of every 5 consecutive days, b) longest subarray with sum ≤ 10, c) max vowels in any substring of length k.
- [ ] **Q5 (code).** LC 643: `max_average(nums, k)`. `[1, 12, -5, -6, 50, 3], k=4` → 12.75.

**Lesson 2: Variable-size window**

- [ ] **Q1.** There's a `while` inside a `for`, yet it's O(n), not O(n²). Why?
- [ ] **Q2 (trace).** `min_len(7, [2, 3, 1, 2, 4, 3])`: show every shrink pass, `left`, `window` and `best`.
- [ ] **Q3.** Why is window length `right - left + 1` and not `right - left`?
- [ ] **Q4.** Build a small array with a negative number where `longest_at_most` returns the wrong answer. Show both answers and explain why.
- [ ] **Q5 (code).** LC 1004, *Max Consecutive Ones III*. `[1,1,1,0,0,0,1,1,1,1,0], k=2` → 6.

**Lesson 3: Python strings**

- [ ] **Q1.** Why can building a string with `+=` in a loop be O(n²)? What's the fix, and why is it O(n)? Use the words *immutable* and *copy*.
- [ ] **Q2.** Predict each line's output or error for `s = "sliding"`: `s[2:5]`, `s[::-1]`, `ord("e") - ord("a")`, `s[0] = "S"`.
- [ ] **Q3.** Time complexity of `sorted(s) == sorted(t)` vs `Counter(s) == Counter(t)`. Which is faster for long strings, and why?
- [ ] **Q4 (code).** LC 242 with a single 26-slot count array. No `sorted` or `Counter`.
- [ ] **Q5 (code).** LC 125 with two pointers and **O(1) extra space**. No cleaned copy of the string.

**Lesson 4: Sliding window on strings**

- [ ] **Q1.** In LC 3, why is checking only `seen[c] > 1` for the new character enough?
- [ ] **Q2 (trace).** `length_of_longest_substring("pwwkew")`, with every shrink pass and its ✓/✗ check.
- [ ] **Q3–Q5.** See "Unfinished Lesson 4 quiz questions" at the top.

## Extra "why" questions

These train explaining *why* something is correct, not *how* the code runs. Answer each in 2–3 sentences with this template:

1. **Claim:** the answer in one line.
2. **Rule:** the general reason (an invariant, a count, a property of the data).
3. **Proof:** one edge case, or an input where the alternative breaks.

- [ ] In `min_len` (shortest window), why is `best` recorded **before** shrinking and not after?
- [ ] In `longest_at_most` (longest window), why is `best` recorded **after** the while loop and not inside it?
- [ ] In LC 3, why must the shrink be a `while` and not an `if`? Give an input where `if` returns the wrong answer.
- [ ] Why does `left` never need to move backward in a variable window?
- [ ] In LC 1004, why is `left += 1` outside the `if nums[left] == 0` check?
- [ ] In `find_anagrams`, why is the check `right >= k` and not `right > k`?
- [ ] Why is a 26-slot count array O(1) space even when the string has a million characters?
- [ ] In the one-array anagram check, why is returning False on a negative count enough, with no final "all zeros" check?
- [ ] Why is `len(s)` O(1) but `s == t` O(n)?
- [ ] Why does the sum-based variable window fail with negative numbers but the zero-counting window in LC 1004 never does?
- [ ] Why does dividing once at the end give the correct max average in LC 643?
- [ ] Why does `s[::-1] == s` use O(n) space while the two-pointer palindrome check uses O(1)?

## Trace drills

Trace by hand. Write every shrink pass on its own line with its ✓/✗ check, and end with `Answer: ...`.

- [ ] `max_sum([5, 1, 3, 7, 2, 6], k=2)`
- [ ] `min_len(11, [1, 2, 3, 4, 5])`
- [ ] `longest_at_most([4, 2, 2, 7, 1, 3], limit=8)`
- [ ] `length_of_longest_substring("abba")`
- [ ] `find_anagrams("abab", "ab")`

Answers to check against (no peeking): 10 · 3 · 3 · 2 · [0, 1, 2]

## LeetCode practice set

Solved ones are ticked. Work top to bottom within each group.

**Fixed window**

- [x] [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) (Easy)
- [ ] [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) (Medium)

**Fixed window + count array**

- [x] [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy, warm-up)
- [ ] [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) (Medium)
- [ ] [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Medium)

**Variable window, longest**

- [x] [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (Medium)
- [ ] [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium)
- [ ] [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) (Medium)
- [ ] [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (Medium, harder)

**Variable window, shortest**

- [ ] [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Medium)
- [ ] [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard, save for last)

**Strings + two pointers**

- [x] [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy, redo with O(1) space)

## Extra LeetCode problems

Once the core set above is done, work through these. Before coding each one, write down which pattern it is and why.

**Fixed window**

- [ ] [1652. Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/) (Easy)
- [ ] [1876. Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) (Easy)
- [ ] [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) (Medium)
- [ ] [2090. K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/) (Medium)

**Variable window, longest**

- [ ] [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) (Medium, close to LC 1004)
- [ ] [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) (Medium, close to LC 3)
- [ ] [1208. Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) (Medium)
- [ ] [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/) (Medium)
- [ ] [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) (Medium, counts windows instead of max length)

**Variable window, shortest**

- [ ] [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) (Medium, tricky reframe)
- [ ] [1234. Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) (Medium)

**Strings: counting and two pointers**

- [ ] [344. Reverse String](https://leetcode.com/problems/reverse-string/) (Easy)
- [ ] [383. Ransom Note](https://leetcode.com/problems/ransom-note/) (Easy, 26-slot array)
- [ ] [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (Easy)
- [ ] [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) (Easy)
- [ ] [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) (Easy)
- [ ] [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) (Medium, practice `join`)
- [ ] [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium)
