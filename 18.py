class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I',]

        res = ""
        for i in range(len(values)):
            while num >= values[i]:
                res += symbols[i]
                num -= values[i]

        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    num1 = 3749
    print(f"Integer: {num1} | Roman: {solution.intToRoman(num1)}")
    
    # Test case 2
    num2 = 58
    print(f"Integer: {num2} | Roman: {solution.intToRoman(num2)}")
    
    # Test case 3
    num3 = 1994
    print(f"Integer: {num3} | Roman: {solution.intToRoman(num3)}")
