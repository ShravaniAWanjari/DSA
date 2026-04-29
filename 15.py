from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left → Right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Right → Left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    ratings1 = [1, 0, 2]
    print(f"Ratings: {ratings1} | Min Candies: {solution.candy(ratings1)}")
    
    # Test case 2
    ratings2 = [1, 2, 2]
    print(f"Ratings: {ratings2} | Min Candies: {solution.candy(ratings2)}")
    
    # Test case 3
    ratings3 = [1, 3, 2, 2, 1]
    print(f"Ratings: {ratings3} | Min Candies: {solution.candy(ratings3)}")