class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_num = set(nums)
        for n in range(len(nums)+1):
            if n not in set_num:
                return n