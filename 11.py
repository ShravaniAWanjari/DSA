from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h_index = i +1
            else:
                break
        return h_index

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    citations1 = [3, 0, 6, 1, 5]
    print(f"Citations: {citations1} | H-Index: {solution.hIndex(citations1)}")
    
    # Test case 2
    citations2 = [1, 3, 1]
    print(f"Citations: {citations2} | H-Index: {solution.hIndex(citations2)}")
    
    # Test case 3
    citations3 = [10, 8, 5, 4, 3]
    print(f"Citations: {citations3} | H-Index: {solution.hIndex(citations3)}")