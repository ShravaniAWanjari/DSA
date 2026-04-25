from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for day in range(len(prices)-1):
            if prices[day+1] - prices[day] > 0:
                total_profit += prices[day+1] - prices[day]
        return total_profit

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices1} | Max Profit: {solution.maxProfit(prices1)}")
    
    # Test case 2
    prices2 = [1, 2, 3, 4, 5]
    print(f"Prices: {prices2} | Max Profit: {solution.maxProfit(prices2)}")
    
    # Test case 3
    prices3 = [7, 6, 4, 3, 1]
    print(f"Prices: {prices3} | Max Profit: {solution.maxProfit(prices3)}")