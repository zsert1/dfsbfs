# N*N행령의 영영생성
# 4이하인 지대 상하좌우로 잠긴다
N=int(input())
totalArea=N*N
graph=[]
for i in range(N):
     graph.append(list(map(int,input().split())))

def dfs(x,y):
     if x <= -1 or x >= N or y <= -1 or y >= N:
          return False
     if graph[x][y]<=4:
          graph[x][y]=5
          if x>=1:
               graph[x-1][y]=4
          if  x < N-1:
               graph[x+1][y]=4
          if y>=1:
               graph[x][y-1]=4
          if  y < N-1:
               graph[x][y+1]=4
          return True
     return False
result=0
for i in range(N):
     for j in range(N):
          if dfs(i,j)==True:
               result+=1
liveArea=totalArea-result
print(liveArea)