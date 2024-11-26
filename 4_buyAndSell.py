from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxProfit=0
        while(r<len(prices)):
                if prices[l]<prices[r]:
                    profit=prices[r]-prices[l]
                    maxProfit=max(profit,maxProfit)
                else:
                    l=r
                r+=1
        return maxProfit
start=True
while(start):
    sol=Solution()
    user_input=list(map(int,input("Enter profits per day [space-separated]:\n").split()))
    result=sol.maxProfit(user_input)
    print(f"The maximum profit is: {result}")