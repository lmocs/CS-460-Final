# Development Log – The Torchbearer

**Student Name:** Logan Moreno
**Student ID:** 827350232

---

## Entry 1 – May 6, 2026: Initial Plan

Before heading straight into an implementation, I want to fully understand the problem by reviewing the instructions and answering the questions in the README. I then want to walk through an example of a potential solution I thought of by hand. Doing this allows me to gather a better idea of how to break down and approach the overall problem. I found that working through each of the parts in order is a natural progression to the solution. I expect Part 5 and 6 to be the hardest, and I plan to test my code by writing my own test cases wherever needed.

---

## Entry 2 – May 11, 2026: Answering README Questions

Following my plan, I went through each of the parts and answered the questions in the README. It took me a bit to understand how to find the time complexity of a single run of Dijkstra's, but after a while I found past notes stepping through a similar problem. I also struggled to understand the worst-case search space of the algorithm. I realized that the algorithm is searching through every possible permutation of nodes in the graph, and found an article online explaining permutations. Taking note of that helped me understand the algorithm's worst-case time complexity.

---

## Entry 3 – May 12, 2026: Start Implementation

After reviewing the README, instructions, and requirements once again, I revisited old lecture notes and previous practice on writing Dijkstra's. Instead of using an array to store distances, I decided to use a dictionary to fit my original answers in the README. Additionally, I started working through a solution by hand for `_explore()`, as I find it easier for me to visualize. I wrote some pseudocode and notes in the function body.

---

## Entry 4 – May 12, 2026: Pass Test Cases Partially

After some trial and error, I finally got test cases to pass partially. Initially, I was getting the correct cost for each test case, but the list of relic chambers in order would be empty. I didn't realize that I was passing in a reference to `relics_visited_order`, which was being updated in the last backtracking step. To fix this, I used the list method `copy()` to assign that to `best[1]`.

---

## Entry 5 – May 13, 2026: Finish Pruning Logic

Proceeded to work on the pruning logic for `_explore()`. Cleaned up comments and other sections of the code.

---

## Entry 6 – May 13, 2026: Post-Implementation Reflection

After finishing my implementation to this problem, I would want to test against multiple different graphs. I tried making my own test cases, but perhaps I overlooked a few edge cases. If I had more time, I would want to ensure that my algorithm is correct and efficient for all possible inputs.

---

## Final Entry – May 13, 2026: Time Estimate

| Part | Estimated Minutes |
|---|---|
| Part 1: Problem Analysis | 10 |
| Part 2: Precomputation Design | 30 |
| Part 3: Algorithm Correctness | 40 |
| Part 4: Search Design | 30 |
| Part 5: State and Search Space | 40 |
| Part 6: Pruning | 40 |
| Part 7: Implementation | 300 |
| README and DEVLOG writing | 30 |
| **Total** | 520 |
