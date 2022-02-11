a= []
for c in range(1,101):
    x = int(input())
    a.append(x)
print(max(a))
print(a.index(max(a))+1)
