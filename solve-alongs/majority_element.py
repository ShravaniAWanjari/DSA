from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        nums1 = set(nums)
        for i in nums1:
            if nums.count(i) > count:
                candidate = i
                count = nums.count(i)
        return candidate

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 2, 3]
    print(f"Nums: {nums1} | Majority Element: {solution.majorityElement(nums1)}")
    
    # Test case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(f"Nums: {nums2} | Majority Element: {solution.majorityElement(nums2)}")