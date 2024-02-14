from collections import deque


def bfs():
    q = deque()
    # 출빌 위치 넣어 준다
    q.append(n)
    while q:
        # 현재 위치를 확인
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        # 이동 거리 계산한다
        for nx in [x - 1, x + 1, x * 2]:
            print(not dist[nx], "not dist[nx]")
            print(dist[nx], " dist[nx]")
            # 방
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


MAX = 10**5  # 최대거리
dist = [0] * (MAX + 1)
n, k = map(int, input().split())
bfs()
