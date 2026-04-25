from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices1} | Max Profit: {solution.maxProfit(prices1)}")
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Prices: {prices2} | Max Profit: {solution.maxProfit(prices2)}")
    
    # Test case 3
    prices3 = [1, 2, 3, 4, 5]
    print(f"Prices: {prices3} | Max Profit: {solution.maxProfit(prices3)}")
