from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))
print(sol.majorityElement([6,5,5]))