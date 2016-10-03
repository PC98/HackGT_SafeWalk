coordinates = []
def condense():
	file = open("AllData.csv", "r")
	fileWrite = open("CondensedData.csv", "w")
	obj = file.read().split("\n")
	for coordinate in obj:
		tmp = coordinate.split(",")
		temporary = []
		temporary.append(tmp[0])
		temporary.append(tmp[1])
		temporary.append(int(tmp[2].split("\r")[0]))
		coordinates.append(temporary)
	i = 0
	while(i<len(coordinates) - 1):
		j = i + 1
		while (j < len(coordinates)):
			if coordinates[i][0][:6] == coordinates[j][0][:6] and coordinates[i][1][:6] == coordinates[j][1][:6]:
			   coordinates[i][2] += coordinates[j][2]
			   coordinates.pop(j)
			   j -= 1
			j += 1
		i += 1
	for data in coordinates:
		fileWrite.write("%s, %s, %d\n" % (data[0], data[1], data[2]))
	file.close()
