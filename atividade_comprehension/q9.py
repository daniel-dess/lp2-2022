p = ['M', 'J', 'L', 'P', 'R']
c = [(i, j) for i in p for j in p if i!=j]
print(c)