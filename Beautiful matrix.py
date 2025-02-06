row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()
row5 = input().split()
def x(y):
    for i in range(len(y)):
        if int(y[i]) == 1:
            return i + 1
            break
        else:
            continue
    return 0


if x(row1) != 0:
    c = 1
    q = x(row1)
elif x(row2) != 0:
    c = 2
    q = x(row2)
elif x(row3) != 0:
    c = 3
    q = x(row3)
elif x(row4) != 0:
    c = 4
    q = x(row4)
else:
    c=5
    q = x(row5)

def s():
    if c >= 3:
        row = c -3
    else:
        row = 3 - c

    if q >= 3:
        column = q -3
    else:
        column = 3 - q

    return row + column

h = s()
print(h)
