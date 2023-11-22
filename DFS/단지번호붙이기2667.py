N=int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))
num=[]
def dfs(x,y):
     if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
     if graph[x][y]==1:
        global count
        count+=1
        graph[x][y]=0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
     
     return False
count=0
result = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count=0
          
           
num.sort()       
print(result)
for i in num:
    print(i)

# 놓친 것 집의 갯수를 세는 count변수와 각 단지별 집의 갯수를 담아 줄 num리스트를 생각하지 못함
# result에 +1를 하기전 count를 num리스트에 담고 그 후 count초기화 
# num sort를 이용하여 정렬
# for문 돌면서 num print하면 해결