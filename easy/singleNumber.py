class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}
        uniq = list(set(nums))
        for num in uniq:
            my_dict[num] = nums.count(num)
        for key in my_dict:
            if my_dict[key] == 1:
                return key
        return -1