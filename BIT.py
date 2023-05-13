class BIT:
    def __init__(self, nums: List[int]):
        self.bits = [0] * (len(nums) + 1)
        self.nums = nums
        self.n = len(nums)
        self.buildBIT()

    def buildBIT(self):
        for i in range(self.n):
            self.updateBIT(i, self.nums[i])  ##nlogn build time

    def queryBIT(self, index):
        cSum = 0
        index += 1
        while index > 0:
            cSum += self.bits[index]
            index -= (index & (-index))
        return cSum

    def updateBIT(self, index, val):
        index += 1
        while index <= self.n:
            self.bits[index] += val
            index += (index & (-index))

    def update(self, index: int, val: int) -> None:
        previous, self.nums[index] = self.nums[index], val
        self.updateBIT(index, val - previous)

    def sumRange(self, left: int, right: int) -> int:
        return self.queryBIT(right) - self.queryBIT(left - 1)

'''
1. BIT and segment tree both 1-index based
2. 0 node is a dummy node in BIT and 0 is unused(not present in the tree) node in segment tree, segment tree root is at 1
3. BIT operation is based on LSB.
3.1 Update: add LSB to current BIT index until index reaches to size, to propagate value of current BIT index from current index to until the BIT size
3.2 Query: subtract LSB from current BIT index until reaches to 0, to collect value in a range 0-i 
3.3 Convert range to 1-index by adding 1 inside the update and query method
3.4 Calculate LSB of a index i = i&(-i)
4. Every BIT node, i represent sum from index i-2^r+1 to i , where r is the position of the least significant non-zero bit in i
5. Size of BIT is number of element+1, size of segment tree is 2n+1; look for how far largest value can go
6. Segment tree element are stored at index n+i

'''
