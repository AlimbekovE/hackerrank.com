case = int(input())
num = str(input())
sinp = num.split()
i = 0
while i < case:
	sinp[i] = int(sinp[i])
	i += 1
t = tuple(sinp)
print(hash(t))
