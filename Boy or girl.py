x = list(input ())
y =[]
for i in x:
    if i in y:
        continue
    else:
        y.append(i)

if (len(y)%2)==1:
    print ("IGNORE HIM")
else:
    print("CHAT WITH HER")
