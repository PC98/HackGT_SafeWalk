import pickle

coordinates = {}


def condense():
    file = open("allcrimelogs.csv", "r")
    # fileWrite = open("CondensedData.csv", "w")
    obj = file.read().split("\n")
    for coordinate in obj:
        tmp = coordinate.split(",")
        key = round(float(tmp[0]), 6), round(float(tmp[1]), 6)
        value = int(tmp[2].split("\r")[0])
        if key in coordinates:
            coordinates[key] += value
        else:
            coordinates[key] = value
    """fileWrite.write("Latitude, Longitude, No. of Crimes\n")
    for data in coordinates:
        fileWrite.write("%s, %s, %d\n" % (data[0], data[1], coordinates[data]))"""
    pickle.dump(coordinates, open( "coordinates.p", "wb" ))
    file.close()
    # fileWrite.close()
condense()
