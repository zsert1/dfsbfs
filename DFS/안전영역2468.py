# N*N행령의 영영생성

N=int(input())
totalArea=N*N
# 지대 최댓값 구하기
max_num=0
graph=[]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(N):
    low = list(map(int, input().split()))
    graph.append(low)
# 들어온 값 지대 최댓값 구하기
    for j in low:
        if j > max_num:
            max_num = j
def dfs(x,y,num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
            if graph[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx,ny,num)

result=0
for i in range(max_num):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j,k,i)
    result = max(result, cnt)
print(result)
# 기존의 문제점
# 최대 높이 값을 결정하는 부분이 제외되어 있었다
# max_num에 최대 높이값을 부여하여 계산
# DFS가 아닌 BFS풀이 해보자!!!