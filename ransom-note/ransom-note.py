class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        magazine_count = Counter(magazine)
        for char in ransomNote:
            if char not in magazine_count:
                return False
            magazine_count[char] -= 1
            if magazine_count[char] == 0:
                del magazine_count[char]
                
        return True
            
            
