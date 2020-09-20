class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float('inf')
        maxProfit = float('-inf')
        for i in range(0, len(prices)):
            if prices[i] < minVal:
                minVal = prices[i]
            elif prices[i] - minVal > maxProfit:
                maxProfit = prices[i] - minVal
        if maxProfit == float('-inf'):
            return 0
        return maxProfit
