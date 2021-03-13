List = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0
i = 0
for x in List:
	while len(List) == 0:
		if x >= 80:
			sum += x
			i +=1
	List = List.pop[0:i]
print(sum)
