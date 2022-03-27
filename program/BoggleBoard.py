def boggleBoard(board, words):
    final_words = {}
    trie = Trie()
    trie.add(words)
    rows = len(board)
    cols = len(board[0])
    visited = [[False for letter in row]for row in board]
    for i in range(rows):
        for j in range(cols):
            DFS(i, j, visited, board, trie.root, final_words)
    return list(final_words.keys())


def DFS(i, j, visited, board, root, final_words):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in root:
        return
    visited[i][j] = True
    root = root[letter]

    if "*" in root:
        final_words[root["*"]] = True
    neighbours = get_neighbours(i, j, board)
    for neighbour in neighbours:
        DFS(neighbour[0], neighbour[1], visited, board, root, final_words)
    visited[i][j] = False


def get_neighbours(i, j, board):
    rows = len(board)
    cols = len(board[0])
    neighbours = []
    if i > 0:
        neighbours.append([i-1, j])
    if i < rows - 1:
        neighbours.append([i+1, j])
    if j > 0:
        neighbours.append([i, j-1])
    if j < cols-1:
        neighbours.append([i, j+1])
    if i > 0 and j > 0:
        neighbours.append([i-1, j-1])
    if i < rows-1 and j < cols-1:
        neighbours.append([i+1, j+1])
    if i < rows-1 and j > 0:
        neighbours.append([i+1, j-1])
    if i > 0 and j < cols-1:
        neighbours.append([i-1, j+1])
    return neighbours


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, words):
        for word in words:
            root = self.root
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
            root[self.endSymbol] = word


board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"]
]
# words = ["this", "is", "not", "a", "simple", "boggle",
#          "board", "test", "REPEATED", "NOTRE-PEATED"]
words = ["boggle", "board", "test", "REPEATED",
         "NOTRE-PEATED", "this", "is", "not", "a"]
print(boggleBoard(board, words))
