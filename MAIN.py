from DataCondenser import condense, coordinates
from Parser import parse
from PointPositionChecker import makeLine

def main():
	parse()
	condense()
	file = open("ParsedJSONoutputForReal.csv", "r")
	data = file.read().split("\n")
	path1 = []
	path2 = []
	for info in data:
		t1 = []
		t2 = []
		tmp = info.split(",")
		if len(tmp[0]) != 0:
			t1.append(float(tmp[0]))
			t1.append(float(tmp[1].split("\r")[0]))
			path1.append(t1)
		t2.append(float(tmp[2]))
		t2.append(float(tmp[3]))
		path2.append(t2)
		
	paths = [path1, path2]
	scores = [0] * 2
	for path in paths:
		for i in range(len(path) - 1):
			for j in coordinates:
				if makeLine(float(j[0]), float(j[1]), path[i][0], path[i][1], path[i+1][0], path[i+1][1]):
					scores[paths.index(path)] += int(j[2])
	print("Path 1 is safer" if scores[0] < scores[1] else "Path 2 is safer")
main()






