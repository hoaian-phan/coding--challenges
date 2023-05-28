class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence_set = set(sentence)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char not in sentence_set:
                return False
        return True