def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    visited = [[-1 for _ in range(len(graph[0]))] for _ in range(len(graph))]

    node = create_node(startRow, startCol, endRow, endCol, 0, None, visited)
    heap = []
    add(heap, node)
    result = []

    while startRow != endRow or startCol != endCol:
        curr_node = remove(heap)
        neighbour = neighbours(curr_node.cell[0], curr_node.cell[1], endRow,
                               endCol, curr_node.g_score, graph, curr_node, visited)
        for nbor in neighbour:
            add(heap, nbor)
        startRow, startCol = curr_node.cell[0], curr_node.cell[1]

    while curr_node != None:
        result.insert(0, curr_node.cell)
        curr_node = curr_node.prev
    return result


def neighbours(currRow, currCol, endRow, endCol, curr_g_score, graph, prev_node, visited):
    neighbours = []
    rows = len(graph)
    cols = len(graph[0])
    if currRow > 0 and graph[currRow-1][currCol] == 0 and visited[currRow-1][currCol] == -1:
        neighbours.append(create_node(currRow-1, currCol, endRow,
                          endCol, curr_g_score + 1, prev_node, visited))

    if currRow < rows-1 and graph[currRow+1][currCol] == 0 and visited[currRow+1][currCol] == -1:
        neighbours.append(create_node(currRow+1, currCol, endRow,
                          endCol, curr_g_score + 1, prev_node, visited))

    if currCol > 0 and graph[currRow][currCol-1] == 0 and visited[currRow][currCol-1] == -1:
        neighbours.append(create_node(currRow, currCol-1, endRow,
                          endCol, curr_g_score + 1, prev_node, visited))

    if currCol < cols-1 and graph[currRow][currCol+1] == 0 and visited[currRow][currCol+1] == -1:
        neighbours.append(create_node(currRow, currCol+1, endRow,
                          endCol, curr_g_score + 1, prev_node, visited))

    return neighbours


def create_node(startRow, startCol, endRow, endCol, g_score, prev_node, visited):
    manhatten_distance = abs(startRow - endRow) + abs(startCol - endCol)
    node = Node([startRow, startCol], g_score, manhatten_distance,
                manhatten_distance + g_score, prev_node)
    visited[startRow][startCol] = manhatten_distance + g_score
    return node


def add(heap, node):
    heap.append(node)
    idx = len(heap)-1
    parent = (idx - 1) // 2
    while idx > 0 and heap[parent].f_score > heap[idx].f_score:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent
        parent = (idx - 1) // 2


def remove(heap):
    if len(heap) == 1:
        return heap.pop()
    return_node = heap[0]
    heap[0] = heap.pop()
    parent = 0
    left = (2 * parent) + 1
    length = len(heap)

    while left < length:
        right = left+1 if left+1 < length else -1
        if right != -1 and heap[right].f_score < heap[left].f_score:
            swap = right
        else:
            swap = left

        if heap[parent].f_score > heap[swap].f_score:
            parent = swap
            left = (2 * parent) + 1
        else:
            return return_node
    return return_node


class Node:
    def __init__(self, cell, g_score, man_dist, f_score, prev):
        self.cell = cell
        self.g_score = g_score
        self.man_dist = man_dist
        self.f_score = f_score
        self.prev = prev


graph = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
print(aStarAlgorithm(0, 1, 4, 3, graph))
