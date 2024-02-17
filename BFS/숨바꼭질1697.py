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
                dist[nx] = (
                    dist[x] + 1
                )  # dist[4,6,10]은 다 1을 가지게 된다. => 이를 노드로 보면 뻗어나가는 것 확인하고 이를 통해 언제 k랑 같아지는지 확인 가능하다
                q.append(nx)


MAX = 10**5  # 최대거리
dist = [0] * (MAX + 1)
n, k = map(int, input().split())
bfs()
