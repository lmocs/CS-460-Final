"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Logan Moreno
Student ID:   827350232

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq
from collections import defaultdict


# =============================================================================
# PART 1
# =============================================================================


def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    return """
## Part 1: Problem Analysis

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
"""


# =============================================================================
# PART 2
# =============================================================================


def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    # Entrance S + Relics in M
    return [spawn] + relics


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    # Initialize data structures for storing shortest-path distances and processing nodes
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        # Pop off the minimum-most node
        curr_dist, curr_node = heapq.heappop(priority_queue)

        # Skip unnecessary iterations
        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_dist = distances[curr_node] + weight

            # Update the path if a lower cost is found
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return distances


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    """
    dist_table = defaultdict(dict)  # Data structure for distance storage

    # Run Dijkstra's on every source node and record their shortest-path distances
    sources = select_sources(spawn, relics, exit_node)
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================


def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    """
    return """
## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  When a node is finalized and added to S, its associated distances are guaranteed to be the cheapest path possible from the source

- **For nodes not yet finalized (not in S):**
  A path may have been found and recorded for the unfinalized node, but it is not necessarily the cheapest path possible

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  Before the first iteration, dist[x] = 0 and the set of finalized nodes S would be empty since no paths from the starting node have been discovered. Therefore, the invariant holds.

- **Maintenance : why finalizing the min-dist node is always correct:**
  Since all edge weights are nonnegative, any other path through an unfinalized node would need to pass through an additional edge, which would only increase the total cost of the path.

- **Termination : what the invariant guarantees when the algorithm ends:**
  After the last iteration, every reachable node is in S and the invariant guarantees each node's recorded distance is the true shortest-path distance from the source.

### Part 3c: Why This Matters for the Route Planner

Recording the correct distance for every possible path between all nodes will allow the route planner to decide which path is the most cost efficient and what order to visit relic chambers.
"""


# =============================================================================
# PART 4
# =============================================================================


def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    """
    return """
## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** If greedy will always pick the nearest unvisited relic chamber first, a locally optimal choice can be more expensive later on. It fails to account for paths that can be locally inoptimal but globally optimal.
- **Counter-example setup:** The following are the nodes in the graph: entrance S, relic chambers A and B, and exit T. Their costs is as follows: S -> A = 1, S -> B = 4, A -> B = 10, A -> T = 1, B -> A = 1, B -> T = 1.
- **What greedy picks:** Greedy will select A first because it is the cheapest (1), then B (10), then exits at T for a total fuel cost of 12.
- **What optimal picks:** Optimal will select B first (4), then A (1), then T for a total fuel cost of 6.
- **Why greedy loses:** In this example, greedy takes the locally optimal choice and selects A first because a cost of 1 is less than B's cost of 4. This fails to account for a cheaper alternative by taking more fuel upfront and saving 6 fuel in the end.

### What the Algorithm Must Explore

- The algorithm must explore every possible order of visiting the relic chambers in M to guarantee that the minimum total fuel cost route is found.
"""


# =============================================================================
# PARTS 5 + 6
# =============================================================================


def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    """
    # Calls `_explore()` and returns the path with the best cost and order
    # Pass `relics` as a set in the corresponding argument
    best = [float("inf"), []]  # Default if there is no valid route

    _explore(
        dist_table=dist_table,
        current_loc=spawn,
        relics_remaining=set(relics),
        relics_visited_order=[],
        cost_so_far=0,
        exit_node=exit_node,
        best=best,
    )

    return tuple(best)


def _explore(
    dist_table,
    current_loc,
    relics_remaining,
    relics_visited_order,
    cost_so_far,
    exit_node,
    best,
):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    """
    # Retrieve the dict of neighbors from the current node
    neighbors = dist_table.get(current_loc)

    # Exit at T and return if there are no more relic chambers to be visited
    if not relics_remaining:
        min_cost_to_exit = neighbors.get(exit_node)
        total_fuel_cost = cost_so_far + min_cost_to_exit

        # If a new minimum-cost path is found, update `best` in place
        if total_fuel_cost < best[0]:
            best[0], best[1] = total_fuel_cost, relics_visited_order.copy()

        return

    # Calculate the lower bound as specified in the README (Part 6)
    min_cost_to_next_relic = min(neighbors.get(relic) for relic in relics_remaining)
    min_cost_relic_to_exit = min(
        dist_table.get(relic).get(exit_node) for relic in relics_remaining
    )
    lower_bound_cost = cost_so_far + min_cost_to_next_relic + min_cost_relic_to_exit

    # Pruning the lower bound cost is safe since it is impossible to get a new
    # minimum fuel cost if the remaining edge weights are greater than or equal
    # to the current best cost. Adding additional nonnegative edges will only
    # increase and exceed the total fuel cost.
    if lower_bound_cost >= best[0]:
        return

    # Iterate through each relic chamber to find all possible orderings
    for relic in relics_remaining:
        # Look up the precomputed cost to the next relic in the set
        cost_to_relic = neighbors.get(relic)

        # Mark the current relic as visited by removing it from the set and adding it to the order
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        # Recurse
        _explore(
            dist_table=dist_table,
            current_loc=relic,
            relics_remaining=relics_remaining,
            relics_visited_order=relics_visited_order,
            cost_so_far=cost_so_far + cost_to_relic,
            exit_node=exit_node,
            best=best,
        )

        # Backtrack
        relics_remaining.add(relic)
        relics_visited_order.remove(relic)


# =============================================================================
# PIPELINE
# =============================================================================


def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================


def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        "S": [("B", 1), ("C", 2), ("D", 2)],
        "B": [("D", 1), ("T", 1)],
        "C": [("B", 1), ("T", 1)],
        "D": [("B", 1), ("C", 1)],
        "T": [],
    }
    cost, order = solve(graph_1, "S", ["B", "C", "D"], "T")
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {"S": [("R", 3)], "R": [("T", 2)], "T": []}
    cost, order = solve(graph_2, "S", ["R"], "T")
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {"S": [("R", 1)], "R": [], "T": []}
    cost, order = solve(graph_3, "S", ["R"], "T")
    assert cost == float("inf"), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        "S": [("X", 1)],
        "X": [("R1", 2), ("R2", 5)],
        "R1": [("Y", 1)],
        "Y": [("R2", 1)],
        "R2": [("T", 1)],
        "T": [],
    }
    cost, order = solve(graph_4, "S", ["R1", "R2"], "T")
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, (
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
        )
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
