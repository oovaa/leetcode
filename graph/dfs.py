n = 5
g = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3],
}
visited = [False, False, False, False, False]


def dfs(at):
    if visited[at]:
        return
    print(f"Visiting node {at}")
    visited[at] = True
    neighbors = g[at]
    for next in neighbors:
        print(f" {at} -> {next}")
        dfs(next)


start = 0
dfs(start)
