import sys



input = sys.stdin.readline

que= []

def push(X):
    que.append(X)
    return que

def pop():
    if len(que) < 1:
        return(-1)
    else:
        que_pop = que.pop(0)
        return que_pop

def size():
    que_n = len(que)
    return que_n
    
def empty():
    if len(que) < 1:
        return(1)
    else:
        return(0)

def front():
    if len(que) < 1:
        return(-1)
    else:
        return que[0]

def back():
    if len(que) < 1:
        return(-1)
    else:
        return que[len(que)-1]
        

a= []
for _ in range(int(input())):
    a = input().split()
    if a[0] == "push": 
        push(int(a[1]))
    elif a[0] == "pop":
        print(pop())

    elif a[0] == "size":
        print(size())

    elif a[0] == "empty":
        print(empty())

    elif a[0] == "front":
        print(front())

    elif a[0] == "back":
        print(back())