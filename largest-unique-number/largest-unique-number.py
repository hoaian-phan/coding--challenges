class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        import collections
        counts = collections.Counter(nums)
        once_list = []
        for key, value in counts.items():
            if value == 1:
                once_list.append(key)
                
        return max(once_list) if once_list else -1