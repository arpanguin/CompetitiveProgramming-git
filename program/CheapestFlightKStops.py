

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # We use two arrays for storing distances and keep swapping
        # between them to save on the memory
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            temp_prices = prices

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices
        return -1 if prices[dst] == float("inf") else prices[dst]


s = Solution()
lst = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
print(s.findCheapestPrice(4, lst, 0, 3, 1))
