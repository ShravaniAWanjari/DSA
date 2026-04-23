from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
                
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    
    print(f"Input 1: nums1={nums1}, m={m}, nums2={nums2}, n={n}")
    solution.merge(nums1, m, nums2, n)
    print(f"Modified nums1: {nums1}\n")  # Expected: [1, 2, 2, 3, 5, 6]
    
    # Test Case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    
    print(f"Input 2: nums1={nums1}, m={m}, nums2={nums2}, n={n}")
    solution.merge(nums1, m, nums2, n)
    print(f"Modified nums1: {nums1}\n")  # Expected: [1]
    
    # Test Case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    
    print(f"Input 3: nums1={nums1}, m={m}, nums2={nums2}, n={n}")
    solution.merge(nums1, m, nums2, n)
    print(f"Modified nums1: {nums1}\n")  # Expected: [1]