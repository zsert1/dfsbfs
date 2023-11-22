N=int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))
zips=dict()
def dfs(x,y):
     if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
     if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
     
     return False
result = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1
            if(result not in zips):
                zips[result]=0
        else:
            if(result in zips):
                 zips[result]=zips[result]+1
           
        
                
        
         
print(result)
print(zips)