class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        count = Counter(stones)
        ans = 0
        for stone in jewels:
            if stone in count:
                ans += count[stone]
        return ans