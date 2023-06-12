class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            while j > -1 and j < len(nums2)-1:
                if nums2[j+1] > nums1[i]:
                    ans[i] = nums2[j+1]
                    break
                else:
                    j += 1
                
        return ans