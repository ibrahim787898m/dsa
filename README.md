# DSA

My data structures and algorithms study, solved in Python, following my own step-by-step roadmap.

Each topic folder holds my notes, the questions I practice, my answers (traces, first attempts and cleaned-up versions), my LeetCode solutions, and my own implementations.

## Progress

| Step  | Topic                                                | Folder                                                                    | Status      |
| ----- | ---------------------------------------------------- | ------------------------------------------------------------------------- | ----------- |
| 1–4   | Big O: concept, time, space, best/worst/average case | [`01_big_o`](python/01_big_o)                                             | Done        |
| 5–6   | Arrays & strings, two pointer technique              | [`05_arrays_strings_two_pointers`](python/05_arrays_strings_two_pointers) | Done        |
| 7–8   | Sliding window, string manipulation                  | [`07_sliding_window_string`](python/07_sliding_window_string)             | Done        |
| 9     | Binary search                                        | [`09_binary_search`](python/09_binary_search)                             | Done        |
| 10    | Linked lists                                         | [`10_linked_list`](python/10_linked_list)                                 | In progress |
| 11    | Reversal                                             |                                                                           | Not started |
| 12    | Fast and slow pointer                                |                                                                           | Not started |
| 13    | Cycle detection                                      |                                                                           | Not started |
| 14    | Stacks & queues                                      |                                                                           | Not started |
| 15    | Sorting algorithms (bubble, merge, quick)            |                                                                           | Not started |
| 16    | Hashing & hash maps                                  |                                                                           | Not started |
| 17    | Recursion basics                                     |                                                                           | Not started |
| 18–20 | Trees: binary trees, BST, traversals                 |                                                                           | Not started |
| 21–23 | Graphs: representation, BFS, DFS                     |                                                                           | Not started |

## Structure

```
dsa/
├── .gitignore
├── LICENSE
├── README.md
└── python/
    └── NN_topic/
        ├── notes.md                concept notes
        ├── practice_questions.md   every question for this topic (questions only)
        ├── quiz/                   my answers to the lesson quizzes, one file per lesson
        │   ├── lesson_1.md
        │   └── lesson_2.md
        ├── extra/                  my answers to the extra practice questions
        │   ├── answers.md          traces and reasoning
        │   └── *.py                code questions as runnable files
        ├── problems/               LeetCode solutions, one file per problem
        │   └── lc_0704_binary_search.py
        ├── rough/                  my rough .txt work (not uploaded, ignored by git)
        └── *.py                    my final, tested implementations
```

- `practice_questions.md` is the question list; everything else in the folder is my answers.
- When I redo a quiz question, the redo goes under my original answer in the same `quiz/` file.
- LeetCode status is tracked in each topic's `practice_questions.md`, linked to the solution in `problems/`.

- Folders are numbered by roadmap step, zero-padded so they sort correctly.
- All folder and file names use snake_case.
- Quiz answers keep my first attempts next to the cleaned-up versions, so the learning shows.
- Each `.py` file starts with a comment: problem link, pattern, time/space complexity, and why the approach works.

## Resources

CS Dojo, NeetCode, VisuAlgo, LeetCode.

Older LeetCode solutions (sorted by difficulty) are in [leetcode-solutions](https://github.com/ibrahim787898m/leetcode-solutions).
