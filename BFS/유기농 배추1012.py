from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    matrix[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if matrix[nx][ny] == 1:
                # 해당 위치를 중심으로 4방향 퍼뜨려야하니 큐에 넣는다
                queue.append((nx, ny))
                # 추가 있는 곳 체크 했으니 없는 곳으로 변경
                matrix[nx][ny] = 0


for i in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * (N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(M):
        for b in range(N):
            # 배추가 있다면
            if matrix[a][b] == 1:
                BFS(a, b)
                cnt += 1
