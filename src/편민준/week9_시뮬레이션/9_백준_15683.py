import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    cnt = 0
    # 사람의 수만큼 반복하여 지목한 사람을 확인
    for _ in range(n):
        target = queue.popleft()
        cnt += 1 

        # 지목한 사람이 보성이의 번호이면 지목 횟수를 리턴
        if graph[target] == k:
            return cnt

        # 지목한 번호를 다시 큐에 추가하여 반복
        queue.append(graph[target])

    # 사람 수만큼 지목이 끝난 후에도 보성이의 번호가 아니면 -1 리턴
    return -1


n, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]

# 0번부터 지목
print(bfs(0))