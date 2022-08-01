import heapq


class Solution:
    """
    Leetcode 505 : The Maze II
    """

    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        heap = [(0, start[0], start[1])]  # (distance, row, col)
        visited = {(start[0], start[1]): 0}  # { (row, col): distance }

        while heap:
            distance, row, col = heapq.heappop(heap)
            if [row, col] == destination:
                return distance
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newR, newC, newD = row, col, distance
                while 0 <= newR + dr < m and 0 <= newC + dc < n and maze[newR+dr][newC+dc] == 0:
                    newR += dr
                    newC += dc
                    newD += 1
                if (newR, newC) not in visited or newD < visited[(newR, newC)]:
                    visited[(newR, newC)] = newD
                    heapq.heappush(heap, (newD, newR, newC))
        return -1


s = Solution()
maze = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(s.shortestDistance(maze, start, destination))
