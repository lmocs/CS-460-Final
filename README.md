# The Torchbearer

**Student Name:** Logan Moreno
**Student ID:** 827350232
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  - A single shortest-path run from S is not enough because it does not have a way to know
    what order to visit each relic and evaluate the combined fuel cost of visiting all relics
    in a specific sequence.

- **What decision remains after all inter-location costs are known:**
  - The order that relic chambers are visited in M from S to T.

- **Why this requires a search over orders (one sentence):**
  - Since different ordering of relic chambers produce different fuel costs, it is important
    to check all possible orderings of relic chambers and to find the one with the minimum
    fuel cost.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Entrance Node S | The Torchbearer's path always starts at S |
| Relic Chamber in M | The Torchbearer stops at each chamber and continues to the next or to the exit T |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary of Dictionaries |
| What the keys represent | Source (outer dict) and Destination (inner dict) |
| What the values represent | The cheapest cost path from source to destination |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Dictionaries have O(1) lookup for all key-value pairs using hash functions |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** One run from S and k runs from each relic chamber (1 + k runs)
- **Cost per run:** O(m * log n), where m is the number of edges and n is the number of vertices in the graph
- **Total complexity:** Number of Runs * Cost Per Run = O(1 + k) * O(m * log n) = O(k * m * log n)
- **Justification (one line):** Since constants are dropped, the time complexity of runs simplifies to O(k) and each run requires one full traversal of the graph from each source k.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  When a node is finalized and added to S, its associated distances are guaranteed to be the cheapest path possible from the source

- **For nodes not yet finalized (not in S):**
  A path may have been found and recorded for the unfinalized node, but it is not necessarily the cheapest path possible

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Before the first iteration, dist[x] = 0 and the set of finalized nodes S would be empty since no paths from the starting node have been discovered. Therefore, the invariant holds.

- **Maintenance : why finalizing the min-dist node is always correct:**
  Since all edge weights are nonnegative, any other path through an unfinalized node would need to pass through an additional edge, which would only increase the total cost of the path.

- **Termination : what the invariant guarantees when the algorithm ends:**
  After the last iteration, every reachable node is in S and the invariant guarantees each node's recorded distance is the true shortest-path distance from the source.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

Recording the correct distance for every possible path between all nodes will allow the route planner to decide which path is the most cost efficient and what order to visit relic chambers.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** If greedy will always pick the nearest unvisited relic chamber first, a locally optimal choice can be more expensive later on. It fails to account for paths that can be locally inoptimal but globally optimal.
- **Counter-example setup:** The following are the nodes in the graph: entrance S, relic chambers A and B, and exit T. Their costs is as follows: S -> A = 1, S -> B = 4, A -> B = 10, A -> T = 1, B -> A = 1, B -> T = 1.
- **What greedy picks:** Greedy will select A first because it is the cheapest (1), then B (10), then exits at T for a total fuel cost of 12.
- **What optimal picks:** Optimal will select B first (4), then A (1), then T for a total fuel cost of 6.
- **Why greedy loses:** In this example, greedy takes the locally optimal choice and selects A first because a cost of 1 is less than B's cost of 4. This fails to account for a cheaper alternative by taking more fuel upfront and saving 6 fuel in the end.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore every possible order of visiting the relic chambers in M to guarantee that the minimum total fuel cost route is found.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | `current_loc` | String | The current node the Torchbearer is at |
| Relics already collected | `relics_remaining` | Set | Relic chambers in M that have not yet been visited |
| Fuel cost so far | `cost_so_far` | Float | Total fuel used to reach the current state |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | Set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | It allows for constant time operations and backtracking |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** k!
- **Why:** Since there are k relic chambers and every possible permutation of the relics must be found, the worst case considered is k! orders.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
