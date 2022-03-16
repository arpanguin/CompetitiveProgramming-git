def rectangle_mania(coords):
    coordsTable = getCoordTable(coords)
    return rectangleCount(coords, coordsTable)


def getCoordTable(coords):
    coordsTable = {}
    for coord in coords:
        coordString = coordToString(coord)
        coordsTable[coordString] = True
    return coordsTable


def rectangleCount(coords, coordsTable):
    rectangle_count = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if not isUpperRight([x1, y1], [x2, y2]):
                continue
            upperCoordsString = coordToString([x1, y2])
            rightCoordsString = coordToString([x2, y1])
            if upperCoordsString in coordsTable and rightCoordsString in coordsTable:
                rectangle_count += 1
    return rectangle_count


def isUpperRight(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return x2 > x1 and y2 > y1


def coordToString(coord):
    x, y = coord
    return str(x) + "-" + str(y)


coords = [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, 3],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0],
    [3, 3]
]
print(rectangle_mania(coords))
