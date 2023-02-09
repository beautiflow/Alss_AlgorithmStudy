t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    dic_arr = {}
    check = []
    count = 0
    cur = 1
    nowCur = 1
    
    for j in range(n):
        dic_arr[j+1] = arr[j]

    while(nowCur <= len(arr)):
        if cur in check:
            nowCur += 1
            cur = nowCur
            if nowCur > len(arr):
                break
        else:
            check.append(cur)
            cur = dic_arr[cur]
            
        if dic_arr[cur] == nowCur:
            check.append(cur)
            nowCur += 1
            cur = nowCur
            count += 1
            
        
    print(count)

