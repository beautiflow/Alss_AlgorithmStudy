ps = int(input())


tvps= ''
tf_vps= []
for _ in range(ps):
    tvps = (input())

    for i in tvps:
        tf_vps.append(i)

    for _ in range(25):
        tvps = tvps.replace('()','')

    print("NO" if tvps else "YES")
