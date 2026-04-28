from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        lastGas = 0

        for i in range(len(gas)):
            lastGas += gas[i] - cost[i]

            if lastGas < 0:
                start = i + 1
                lastGas = 0
        return start

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    print(f"Gas: {gas1}, Cost: {cost1} | Start Index: {solution.canCompleteCircuit(gas1, cost1)}")
    
    # Test case 2
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    print(f"Gas: {gas2}, Cost: {cost2} | Start Index: {solution.canCompleteCircuit(gas2, cost2)}")