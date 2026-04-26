from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    print(f"Nums: {nums1} | Min Jumps: {solution.jump(nums1)}")
    
    # Test case 2
    nums2 = [2, 3, 0, 1, 4]
    print(f"Nums: {nums2} | Min Jumps: {solution.jump(nums2)}")
    
    # Test case 3
    nums3 = [1, 2, 3]
    print(f"Nums: {nums3} | Min Jumps: {solution.jump(nums3)}")