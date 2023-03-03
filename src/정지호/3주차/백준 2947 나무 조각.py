li = input().split()

while(li != ["1", "2", "3", "4", "5"]):
    if int(li[0]) > int(li[1]):
        li[0], li[1] = li[1], li[0]
        print(" ".join(li))

    if int(li[1]) > int(li[2]):
        li[1], li[2] = li[2], li[1]
        print(" ".join(li))

    if int(li[2]) > int(li[3]):
        li[2], li[3] = li[3], li[2]
        print(" ".join(li))

    if int(li[3]) > int(li[4]):
        li[3], li[4] = li[4], li[3]
        print(" ".join(li))