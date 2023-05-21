class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                results[i] = nums[right] * nums[right]
                right -= 1
            else:
                results[i] = nums[left] * nums[left]
                left += 1
                
        
        return results
        
        
                
                