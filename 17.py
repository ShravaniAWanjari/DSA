class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        total = 0

        for i in range(len(s)):
            if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "III"
    print(f"Roman: {s1} | Integer: {solution.romanToInt(s1)}")
    
    # Test case 2
    s2 = "LVIII"
    print(f"Roman: {s2} | Integer: {solution.romanToInt(s2)}")
    
    # Test case 3
    s3 = "MCMXCIV"
    print(f"Roman: {s3} | Integer: {solution.romanToInt(s3)}")