from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+= 1
        return k

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    print(f"Input: nums = {nums1}, val = {val1}")
    k1 = solution.removeElement(nums1, val1)
    print(f"Output: k = {k1}, nums = {nums1[:k1]}\n")
    
    # Test Case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(f"Input: nums = {nums2}, val = {val2}")
    k2 = solution.removeElement(nums2, val2)
    print(f"Output: k = {k2}, nums = {nums2[:k2]}\n")