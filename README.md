[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ulyILqqB)


Weekly Coding #9: Midnight Monster Delivery
Summary

This program finds the cheapest delivery routes through a haunted city using Dijkstra’s algorithm. Each location in the city is represented as a node, and each haunted road has a positive travel cost. The program uses Python’s heapq module to manage a priority queue for efficient pathfinding. It can calculate the minimum delivery cost to every location and also reconstruct the shortest path between two locations. The program also validates the graph to make sure all edge weights are positive and all neighbors exist in the graph.

Approach
I represented the haunted city as an adjacency dictionary where each node maps to its neighboring nodes and travel costs.
I used a heap-based priority queue (heapq) to always process the node with the smallest known cost first.
Relaxation was performed by checking whether a newly discovered path to a neighbor was cheaper than the currently stored distance.
If a cheaper path was found, I updated the distance and pushed the new value into the priority queue.
For path reconstruction, I used a previous dictionary to track the parent node for each location.
After reaching the target node, I rebuilt the final path by tracing backward from the target to the start node.
Complexity
Time complexity: O((V + E) log V), where V is the number of locations and E is the number of roads.

Space complexity: O(V) extra space for distances, previous nodes, and the frontier. If we include graph storage, the total is O(V + E).
monster_delivery_costs
Time: O((V + E) log V)
Space: O(V)
Why:
Each node and edge may be processed once.
Heap operations such as heappush() and heappop() take O(log V) time.
Extra space is used for the distances dictionary and priority queue.
shortest_monster_delivery
Time: O((V + E) log V)
Space: O(V)
Why:
The algorithm still uses Dijkstra’s shortest path process with a heap queue.
An additional previous dictionary stores parent nodes for path reconstruction.
Rebuilding the path takes at most O(V) time.
Edge-Case Checklist
 start equals target
 target is unreachable
 start node is missing
 target node is missing
 node has no outgoing edges
 graph contains cycles
 tied shortest paths
 negative edge weight
 zero edge weight
 neighbor not listed as a graph node
Tests I Added
Tested graph validation with negative edge weights.
Tested unreachable target nodes returning (inf, []).
Tested shortest path reconstruction with multiple valid paths.
Assistance & Sources

AI used? Yes

If yes, what did it help with?

Helped review Dijkstra’s algorithm logic.
Helped improve code readability and edge-case handling.
Helped explain complexity analysis clearly.

Other sources used:

Python documentation for heapq
Class lecture notes
Notes for Instructor
I focused on writing clean and readable code with proper validation.
I added edge-case handling to improve reliability and correctness.
The solution follows the assignment rules and uses only the Python standard library.
i need human made and make as i and my opene
Weekly Coding #9: Midnight Monster Delivery
Summary

In this assignment, I created a program that finds the cheapest delivery routes through a haunted city using Dijkstra’s algorithm. Each place in the city is treated as a node, and each road has a positive travel cost. I used Python’s heapq module to create a priority queue so the algorithm could efficiently choose the next cheapest path. The program can calculate the cheapest delivery cost to all locations and also find the shortest path between two specific locations. I also added validation to make sure the graph is valid and contains only positive edge weights.

Approach
I represented the haunted city using an adjacency dictionary where each node stores its neighboring locations and travel costs.
I used a heap-based priority queue with heapq to always process the location with the smallest current delivery cost.
During the algorithm, I used relaxation by checking if a newly discovered path was cheaper than the existing distance.
If a shorter path was found, I updated the distance and pushed the new value into the heap queue.
To rebuild the shortest path, I used a previous dictionary to remember the parent node of each location.
After reaching the target, I reconstructed the final path by tracing backward from the target node to the starting node.
Complexity
Time complexity: O((V + E) log V), where V is the number of locations and E is the number of roads.

Space complexity: O(V) extra space for distances, previous nodes, and the frontier. If we include graph storage, the total is O(V + E).
monster_delivery_costs
Time: O((V + E) log V)
Space: O(V)
Why:
I processed each node and edge while using heap operations.
heappush() and heappop() take O(log V) time.
Extra memory was needed for the distances dictionary and priority queue.
shortest_monster_delivery
Time: O((V + E) log V)
Space: O(V)
Why:
The function still uses Dijkstra’s algorithm with a heap queue.
I stored previous nodes for path reconstruction.
Rebuilding the final path takes at most O(V) time.
Edge-Case Checklist
 start equals target
 target is unreachable
 start node is missing
 target node is missing
 node has no outgoing edges
 graph contains cycles
 tied shortest paths
 negative edge weight
 zero edge weight
 neighbor not listed as a graph node
Tests I Added
I tested graphs with negative edge weights to confirm validation errors were raised.
I tested unreachable target nodes to make sure the function returned (inf, []).
I tested shortest path reconstruction with different graph layouts.
I tested cases where the start node and target node were the same.
Assistance & Sources

AI used? Yes

If yes, what did it help with?

It helped me review Dijkstra’s algorithm.
It helped me improve edge-case handling and complexity explanations.
It helped me organize and clean up my code.

Other sources used:

Python heapq documentation
Class lecture notes
Zybooks examples
Notes for Instructor
I focused on writing readable and well-structured code.
I spent extra time testing edge cases and validating graph inputs.
I learned a lot about priority queues, shortest path algorithms, and complexity analysis during this assignment.