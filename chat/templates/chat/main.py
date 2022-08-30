x = [1, 2, 3]
y = x
y.append(4)
print(x)

s = '123'
t = s
t = t + '123'
print(t is s)