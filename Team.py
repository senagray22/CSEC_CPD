x = int(input())
d = 0
def y():
    global d
    for i in range(x):
        y = input().split()
        h = 0
        for i in y:
            if i == "1":
                h += 1
            else:
                continue
        if h > 1:
            d +=1
        else:
            continue
y()
print(d)
