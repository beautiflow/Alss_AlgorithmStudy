import sys

n = int(input())
deck = []

input = sys.stdin.readline

for i in range(n):
    order = list(input().split())
    if order[0] == "push_front":
        deck.insert(0,order[1])

    elif order[0] == "push_back":
        deck.append(order[1])

    elif order[0] == "pop_front":
        if deck:
            a = deck.pop(0)
            print(a)
        else:
            print(-1)

    elif order[0] == "pop_back":
        if deck:
            a = deck.pop()
            print(a)
        else:
            print(-1)

    elif order[0] == "size":
        print(len(deck))
        
    elif order[0] == "empty":
        if deck:
            print(0)
        else:
            print(1)
    
    elif order[0] == "front":
        if deck:
            print(deck[0])
        else:
            print(-1)
    
    elif order[0] == "back":
        if deck:
            print(deck[-1])
        else:
            print(-1)