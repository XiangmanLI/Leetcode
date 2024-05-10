class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp = 0
        buy = prices[0]
        sell =0
        i = 1
        for i in range(len(prices)):
            tmp = prices[i] - buy
            if sell < tmp:
                sell = tmp
            if buy > prices[i]:
                buy = prices[i]
            #i+=1

        return sell
            
        
