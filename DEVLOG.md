# Development Log – The Torchbearer

**Student Name:** Logan Moreno
**Student ID:** 827350232

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – May 6, 2026: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

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

## Entry 5 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
