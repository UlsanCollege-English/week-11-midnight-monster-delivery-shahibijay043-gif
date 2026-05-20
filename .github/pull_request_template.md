What I changed
Implemented Dijkstra’s algorithm using heapq.
Added graph validation for invalid weights and missing neighbor nodes.
Improved shortest path reconstruction and edge-case handling.
Standards claimed

Core:

S12
S11
S3
Electives, if any:
Evidence
 pytest -q passes
 README updated with approach, complexity, and edge cases
 Added/updated tests for edge cases
Notes for reviewer
I focused on clean code structure, readability, and handling special edge cases correctly.
Added extra testing for unreachable targets and invalid graph inputs.