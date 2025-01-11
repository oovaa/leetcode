import queue

n = 5
g = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2],
}


def solve(s):
    q = queue.Queue()
    q.put(s)
    visited = [False, False, False, False, False]
    visited[s] = True
    prev = [None, None, None, None, None]

    print(f"Starting BFS from node {s}")

    while not q.empty():
        node = q.get()
        print(f"Visiting node {node}")

        neighbors = g.get(node)

        for next in neighbors:
            if not visited[next]:
                q.put(next)
                visited[next] = True
                prev[next] = node
                print(f"Queueing node {next} and setting its predecessor to {node}")
    return prev


def reconstruct(s, e, prev):
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()

    if path[0] == s:
        print(f"Path found: {path}")
        return path
    print("No path found")
    return []


def bfs(s, e):
    prev = solve(s)
    return reconstruct(s, e, prev)


# Example usage
if __name__ == "__main__":
    start_node = 0
    end_node = 4
    print(f"Finding path from {start_node} to {end_node}")
    path = bfs(start_node, end_node)
    print(f"Path: {path}")
