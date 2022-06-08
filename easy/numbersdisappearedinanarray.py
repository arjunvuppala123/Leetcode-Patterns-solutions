class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_nums = len(nums)
        arr = [i for i in range(1,max_nums+1)]
        missing = []
        nums = set(nums)
        for i in arr:
            if i not in nums:
                missing.append(i)
        return missing