n = int(input())
line = str(input())
arr = line.split()
i = 0
while i < n:
	arr[i] = int(arr[i])
	i += 1
arr.sort()
arr.reverse()
max_score = arr[0]
i = 0
while i < n:
	if arr[i] != max_score:
		break
	i += 1
print(arr[i])
