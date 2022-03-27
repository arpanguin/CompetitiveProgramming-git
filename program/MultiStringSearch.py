def multiStringSearch(bigString, smallStrings):
    lenght_of_small_str = len(smallStrings)
    output = [False for _ in range(lenght_of_small_str)]
    tries = Tries()
    for i in range(lenght_of_small_str):
        tries.insert(smallStrings[i], i)
    check_string_existance(bigString, output, tries)
    return output


def check_string_existance(bigString, output, tries):
    lenght_of_big_str = len(bigString)
    current_root = tries.root
    for i in range(lenght_of_big_str):
        for j in range(i, lenght_of_big_str):
            char = bigString[j]
            if char not in current_root:
                current_root = tries.root
                continue
            current_root = current_root[char]
            if tries.endSymbol in current_root:
                output[current_root[tries.endSymbol]] = True


class Tries:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string, index):
        current_root = self.root
        for i in range(len(string)):
            char = string[i]
            if char not in current_root:
                current_root[char] = {}
            current_root = current_root[char]
        current_root[self.endSymbol] = index


bigString = "abcdefghijklmnopqrstuvwxyz"
smallStrings = ["abc", "abcdef", "mnopqr", "wyz", "no", "e", "tuuv"]
print(multiStringSearch(bigString, smallStrings))
