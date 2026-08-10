class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minLeft = [0,10,1,1,1,1]
        # prices = [10,1,5,6,7,1]
        # maxProfit = [0,]
        
        maxProfit = 0
        minLeft = 101
        minLeft_arr = []
        for i in range(len(prices)):
            if i == 0:
                minLeft_arr.append(minLeft)
            elif i == 1:
                minLeft = prices[i-1]
                minLeft_arr.append(minLeft)
            else:
                minLeft = min(minLeft,prices[i-1])
                minLeft_arr.append(minLeft)
        print(minLeft_arr)

        for i in range(len(prices)):
            maxProfit = max(prices[i] - minLeft_arr[i], maxProfit)
        return maxProfit
