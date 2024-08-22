class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for idx, word in enumerate(words):
            if x in word:
                indices.append(idx)
        return indices
        
