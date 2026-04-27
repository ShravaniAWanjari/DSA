import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        self.arr[idx],self.arr[-1] = self.arr[-1],self.arr[idx]
        self.map[self.arr[idx]] = idx
        self.arr.pop()
        del self.map[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)
        


if __name__ == "__main__":
    # Initialize the RandomizedSet
    obj = RandomizedSet()
    
    # Test cases
    print(f"Insert 1: {obj.insert(1)}")        # Expected: True
    print(f"Remove 2: {obj.remove(2)}")        # Expected: False
    print(f"Insert 2: {obj.insert(2)}")        # Expected: True
    print(f"GetRandom: {obj.getRandom()}")     # Expected: 1 or 2
    print(f"Remove 1: {obj.remove(1)}")        # Expected: True
    print(f"Insert 2: {obj.insert(2)}")        # Expected: False (already exists)
    print(f"GetRandom: {obj.getRandom()}")     # Expected: 2