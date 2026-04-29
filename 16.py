from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        water = 0

        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])

        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        for i in range(n):
            water += min(left_max[i],right_max[i]) - height[i]

        return water

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Height: {height1} | Trapped Water: {solution.trap(height1)}")
    
    # Test case 2
    height2 = [4,2,0,3,2,5]
    print(f"Height: {height2} | Trapped Water: {solution.trap(height2)}")
    
    # Test case 3
    height3 = [1, 2, 3, 4]
    print(f"Height: {height3} | Trapped Water: {solution.trap(height3)}")