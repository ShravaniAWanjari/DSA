from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            char = strs[0][i]

            for j in strs:
                if i >= len(j) or j[i] != char:
                    return strs[0][:i]

        return strs[0]

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["ab", "a"], "a"),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["apple", "ape", "april"], "ap"),
        ([""], ""),
        (["a"], "a")
    ]
    
    for i, (strs, expected) in enumerate(test_cases):
        result = solution.longestCommonPrefix(strs)
        status = "✅ PASS" if result == expected else f"❌ FAIL (Expected: '{expected}', Got: '{result}')"
        print(f"Test Case {i+1}: {strs} => '{result}' {status}")
