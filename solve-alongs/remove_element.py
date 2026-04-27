from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        nums1 = []
        for i in range(len(nums)):
            if nums[i] != val:
                nums1.append(nums[i])
                k+=1
        
        nums[:] = nums1[:]
        return k

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Nums: [3, 2, 2, 3], Val: 3 | k: {k1}, Modified Nums: {nums1[:k1]}")
    
    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Nums: [0, 1, 2, 2, 3, 0, 4, 2], Val: 2 | k: {k2}, Modified Nums: {nums2[:k2]}")