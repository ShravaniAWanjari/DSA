from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return len(nums)

        k = 2

        for i in range(2,len(nums)):
            if nums[i]!= nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases for "at most 2 duplicates allowed"
    test_cases = [
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [1, 2, 3],
        [1, 1, 1, 1, 1],
        []
    ]
    
    print("🚀 Testing removeDuplicates (at most 2 duplicates)...")
    print("-" * 50)
    
    for i, nums in enumerate(test_cases):
        original = list(nums)
        k = sol.removeDuplicates(nums)
        print(f"Test Case {i + 1}:")
        print(f"  Input:    {original}")
        print(f"  Result k: {k}")
        print(f"  Modified: {nums[:k]}")
        print("-" * 50)
