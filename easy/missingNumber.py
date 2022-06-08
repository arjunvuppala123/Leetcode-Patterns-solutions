class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        obs_sum = sum(nums)
        actSum = 0
        for i in range(1,len(nums)+1):
            actSum += i
        return actSum-obs_sum
    