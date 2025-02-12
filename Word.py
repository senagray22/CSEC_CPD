x = input()
l=[]
z=[]
for i in x:
    if i.upper() == i:
        l.append(i)
    else:
        z.append(i)

if len(l)>len(z):
    print(x.upper())
else:
    print(x.lower())
