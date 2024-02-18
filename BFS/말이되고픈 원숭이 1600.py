from collections import deque

K = int(input())
W, H = map(int, input().split())
graph = list(map(lambda x: list(map(int, input().split())), range(H)))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dhx = [-2, -2, -1, -1, 1, 1, 2, 2]
dhy = [1, -1, 2, -2, 2, -2, -1, 1]


def bfs():
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = True
    queue = deque([(0, 0, K, 0)])
    while queue:
        x, y, k, move = queue.popleft()
        if x == H - 1 and y == W - 1:
            return move

        if k:
            for i in range(8):
                nx = x + dhx[i]
                ny = y + dhy[i]

                if (
                    0 <= nx < H
                    and 0 <= ny < W
                    and not visited[nx][ny][k - 1]
                    and graph[nx][ny] != 1
                ):
                    visited[nx][ny][k - 1] = True
                    queue.append((nx, ny, k - 1, move + 1))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < H
                and 0 <= ny < W
                and not visited[nx][ny][k]
                and graph[nx][ny] != 1
            ):
                visited[nx][ny][k] = True
                queue.append((nx, ny, k, move + 1))
    return -1


print(bfs())
