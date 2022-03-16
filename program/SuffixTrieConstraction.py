class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.addNode(i, string)

    def addNode(self, i, string):
        currentNode = self.root
        for j in range(i, len(string)):
            char = string[j]
            if char not in currentNode:
                currentNode[char] = {}
            currentNode = currentNode[char]
        currentNode[self.endSymbol] = True

    def contains(self, string):
        current_node = self.root
        for i in range(len(string)):
            if string[i] not in current_node:
                return False
            current_node = current_node[string[i]]
        return self.endSymbol in current_node


trie = SuffixTrie("babc")
print(trie.contains("abc"))
