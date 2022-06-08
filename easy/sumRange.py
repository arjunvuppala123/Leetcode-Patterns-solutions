class NumArray:

    def __init__(self, nums: List[int]):
        self.accumulate = [0]
        for num in nums:
            self.accumulate += [self.accumulate[-1] + num]

    def sumRange(self, left: int, right: int) -> int:
        return self.accumulate[right+1] - self.accumulate[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

numArray = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = numArray.sumRange(2,5)