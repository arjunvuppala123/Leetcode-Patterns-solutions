class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        uniq_nums = list(set(nums))
        for num in uniq_nums:
            count[num] = nums.count(num)
        count = dict({k: v for k, v in sorted(count.items(), key=lambda item: item[1])})
        res = list(count.keys())
        return res[-1]