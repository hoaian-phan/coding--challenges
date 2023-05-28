class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        dictionary = {num:ind for ind, num in enumerate(arr)}
        for ele in arr:
            if ele + 1 in dictionary:
                count += 1
        return count
        