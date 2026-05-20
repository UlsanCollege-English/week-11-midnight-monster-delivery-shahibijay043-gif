from math import inf
import heapq


def validate_haunted_map(graph: dict[str, dict[str, int]]) -> None:
    """Raise ValueError if the haunted map is invalid."""

    if not isinstance(graph, dict):
        raise ValueError("Graph must be a dictionary.")

    for node, neighbors in graph.items():
        if not isinstance(neighbors, dict):
            raise ValueError(f"{node} must map to a dictionary.")

        for neighbor, weight in neighbors.items():
            if neighbor not in graph:
                raise ValueError(f"Unknown neighbor: {neighbor}")

            if weight <= 0:
                raise ValueError("Edge weights must be positive.")


def monster_delivery_costs(
    graph: dict[str, dict[str, int]],
    start: str,
) -> dict[str, float]:
    """Return the cheapest delivery cost from start to every location."""

    validate_haunted_map(graph)

    if start not in graph:
        raise ValueError("Start node is missing.")

    distances = {node: inf for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_cost > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor),
                )

    return distances


def shortest_monster_delivery(
    graph: dict[str, dict[str, int]],
    start: str,
    target: str,
) -> tuple[float, list[str]]:
    """Return the cheapest cost and path from start to target."""

    validate_haunted_map(graph)

    if start not in graph or target not in graph:
        return (inf, [])

    if start == target:
        return (0, [start])

    distances = {node: inf for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_cost > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor),
                )

    if distances[target] == inf:
        return (inf, [])

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return (distances[target], path)


def best_next_monster_stop(
    graph: dict[str, dict[str, int]],
    start: str,
    targets: list[str],
) -> tuple[str, float]:
    """Return the reachable target with the cheapest delivery cost."""

    validate_haunted_map(graph)

    if start not in graph:
        return ("", inf)

    distances = monster_delivery_costs(graph, start)

    best_target = ""
    best_cost = inf

    for target in targets:
        if target in distances and distances[target] < best_cost:
            best_target = target
            best_cost = distances[target]

    return (best_target, best_cost)