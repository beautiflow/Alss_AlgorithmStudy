""" 
1. 상하좌우로 연결된 그림의 크기를 알아내기
=> 큐에서 pop을 몇번하는지만 세리면 끝

2. 도화지에 있는 모든 그림을 찾아내기 
=> 한시작점만을 찾아내는 법만을 알고있기 때문에
"""


from collections import deque
N, M = map(int,input().split())

# 방문 유무확인
vis = [[False] * M for _ in range(N)]

# N줄 만큼 입력
board = [list(map(int, input().split())) for _ in range(N)]

# 아래 오른 위 왼쪽 순으로 탐색배열
dx = [1,0,-1,0]
dy = [0,1,0,-1]

result = []

def bfs(x, y):
  count = 1 # 첫번째 들어온 좌표는 그림이므로 1로 잡아준다.
    # 범위 벗어나면 중단
  q = deque() # 탐색을 도와주는 큐
  q.append([x, y])  #시작점을 큐에넣기
  while q:
    x, y = q.popleft()
    
   # 아래 오른 위 왼쪽 순으로 탐색배열
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
    # 범위 안에 있는데, 방문을 안했고, 값이 1이다면 그림으로 판단!
      if 0<=nx<N and 0<=ny<M:      
        if vis[nx][ny] == False and board[nx][ny] == 1:
          count += 1
          vis[nx][ny] = True
          q.append([nx, ny])
  return count
        


# 열
for x in range(N):
  # 행
  for y in range(M):
  # 현재 있는 위치가 그림이고, 방문을 안했으면? 시작!
    if board[x][y] == 1 and vis[x][y] == False: 
      vis[x][y] = True
      pic = bfs(x,y)
      result.append(pic)


if len(result)== 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))
    
    
    
    
    
    
    
'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''