first = input()
x = first.split()
second = input()
y = second.split()
z=0
def main():
  global z
  for i in range(int(x[0])):
    if int(x[1])>= int(y[i]):
      z = z + 1
    else:
      z = z + 2
  return z
x=main()
print(x)
