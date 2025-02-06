x = int(input())
y = input()
z = 0
f = 0
def main():
    global z,f
    for i in y:
        if i == "A":
            z = z + 1
        else:
            f = f + 1
    return z ,f
main()
if z > f:
    print("Anton")
elif z < f:
    print("Danik")
else:
    print('Friendship')
