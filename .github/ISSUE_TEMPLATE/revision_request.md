---
name: Revision Request
about: Request re-evaluation for specific standards
labels: ["revision"]
---

Student
Name: Bijay
Repo: 2412083
Standards to re-check

List the standard IDs:

 S12
 S11
 S3
 Other:
Link to PR / commits
PR link:
Commit hash, if needed:
What changed
Fixed Dijkstra’s algorithm implementation using heapq.
Added graph validation for invalid edge weights and missing nodes.
Improved shortest path reconstruction and edge-case handling.
Feedback addressed

Copy the key feedback points you fixed:

Added proper validation for negative and zero edge weights.
Fixed unreachable path handling and missing node cases.
Self-check
 All tests pass locally with pytest -q
 README includes time/space complexity and edge cases
 I added or updated tests for the bug I fixed