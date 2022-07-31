class Solution:
    """
    Leetcode 490 : The Maze
    """

    def hasPath(self, maze, start, destination):
        row, col = len(maze), len(maze[0])
        stack = [start]
        while stack:
            x, y = stack.pop()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x_, y_ = x, y
                while 0 <= x_ < row and 0 <= y_ < col and maze[x_][y_] != 1:
                    x_ += dx
                    y_ += dy
                x_ -= dx
                y_ -= dy
                if [x_, y_] == destination:
                    return True
                elif maze[x_][y_] == 0:
                    maze[x_][y_] = 2
                    stack.append([x_, y_])
                else:
                    continue
        return False


s = Solution()
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(s.hasPath(maze, start, destination))
