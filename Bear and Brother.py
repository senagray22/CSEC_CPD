e= input()
z= e.split()
limak = int(z[0])
bob = int(z[1])
def x ():
    z =0
    global limak, bob
    while True:
        z += 1
        if limak <= bob:
            limak *= 3
            bob *= 2
            if limak > bob:
                break
        else:
            break
    return z
y = x()
print(y)
