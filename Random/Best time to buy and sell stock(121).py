class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        buy = prices[0]
        for i in range(len(prices)):
            if(buy<prices[i]):
                cp = prices[i]-buy
                p = max(p,cp)
            else:
                buy = prices[i]
        return p
        
