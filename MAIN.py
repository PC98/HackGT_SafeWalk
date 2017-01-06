import pickle
from Parser import parse, set_of_coordinates
from PointPositionChecker import make_line


def main():
    parse()
    num_of_routes = len(set_of_coordinates)
    i = 0
    pos = 0
    minimum = 500
    coordinates = pickle.load(open( "coordinates.p", "rb" ))
    while i < num_of_routes:
        j = 0
        unsafe_score = 0
        num_of_steps = len(set_of_coordinates[i])
        while j < num_of_steps - 1:
            for coordinate in coordinates:
                if make_line(coordinate[0], coordinate[1], set_of_coordinates[i][j][0], set_of_coordinates[i][j][1],
                             set_of_coordinates[i][j + 1][0], set_of_coordinates[i][j + 1][1]):
                    unsafe_score += coordinates[coordinate]
            j += 1
        if unsafe_score < minimum:
            minimum = unsafe_score
            pos = i
        i += 1
    print("Path %d is safer with an unsafety score of %d" % (pos + 1, minimum))


main()
