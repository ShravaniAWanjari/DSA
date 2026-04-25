from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] *26

            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {strs1}")
    print(f"Output: {solution.groupAnagrams(strs1)}")
    
    # Test case 2
    strs2 = [""]
    print(f"\nInput: {strs2}")
    print(f"Output: {solution.groupAnagrams(strs2)}")
    
    # Test case 3
    strs3 = ["a"]
    print(f"\nInput: {strs3}")
    print(f"Output: {solution.groupAnagrams(strs3)}")