from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums1 = [0]*len(nums)
        for i in range(len(nums)):
            idx = (i+k)%len(nums)
            nums1[idx] = nums[i]
        nums[:] = nums1[:]

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    print(f"Original 1: {nums1}, k: {k1}")
    solution.rotate(nums1, k1)
    print(f"Rotated 1:  {nums1}")
    
    # Test Case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    print(f"\nOriginal 2: {nums2}, k: {k2}")
    solution.rotate(nums2, k2)
    print(f"Rotated 2:  {nums2}")
    
    # Test Case 3 (k > len(nums))
    nums3 = [1, 2]
    k3 = 3
    print(f"\nOriginal 3: {nums3}, k: {k3}")
    solution.rotate(nums3, k3)
    print(f"Rotated 3:  {nums3}")
