from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_data = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1, 2, 3],
        [],
        [1, 1, 1]
    ]
    
    print("🚀 Running removeDuplicates tests...")
    print("-" * 40)
    
    for i, nums in enumerate(test_data):
        # We make a copy because the method might (conceptually) modify it
        original = list(nums)
        count = sol.removeDuplicates(nums)
        
        print(f"Test Case {i + 1}:")
        print(f"  Input:  {original}")
        print(f"  Result: {count} unique elements")
        print("-" * 40)
