from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = 1
    
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right
            right  *= nums[i]  
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(f"Nums: {nums1} | Result: {solution.productExceptSelf(nums1)}")
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Nums: {nums2} | Result: {solution.productExceptSelf(nums2)}")