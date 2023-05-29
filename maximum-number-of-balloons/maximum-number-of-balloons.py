class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        import collections
        if len(text) < len('balloon'):
            return 0
        
        counter = collections.Counter(text)

        counter['l'] //= 2
        counter['o'] //= 2

        return min(counter['b'], 
                   counter['a'], 
                   counter['l'], 
                   counter['o'],
                   counter['n'])
        

            
            