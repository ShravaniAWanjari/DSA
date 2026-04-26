from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach  = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach,i + nums[i])
        return True

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    print(f"Nums: {nums1} | Can Jump: {solution.canJump(nums1)}")
    
    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    print(f"Nums: {nums2} | Can Jump: {solution.canJump(nums2)}")
    
    # Test case 3
    nums3 = [0]
    print(f"Nums: {nums3} | Can Jump: {solution.canJump(nums3)}")