class SegmenTree:
    def __init__(self, n):
        self.size = n
        self.sTree = [0] * (2 * n + 1)

    def build(self):
        for i in range(self.size - 1, 0, -1):
            self.sTree[i] = max(self.sTree[i << 1], self.sTree[i << 1 | 1])

    def update(self, index, val):
        index += self.size
        self.sTree[index] += val

        while index > 1:
            index >>= 1
            # same as self.sTree[index] = max(self.sTree[2*index], self.sTree[2*index+1])
            self.sTree[index] = max(self.sTree[index << 1], self.sTree[index << 1 | 1])

    def query(self, l, r):  # excluding r, range l to r-1
        l += self.size
        r += self.size
        maxLen = 0

        while l < r:
            if l & 1:  # if odd, l is right child
                maxLen = max(maxLen, self.sTree[l])
                l += 1
            if r & 1:  # if odd, r is right child
                r -= 1
                maxLen = max(maxLen, self.sTree[r])
            l >>= 1
            r >>= 1
        return maxLen

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

if __name__ == "__main__":
    seg_tree = SegmenTree()