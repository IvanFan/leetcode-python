class ShortestWordDistance:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        wordA = -1
        wordB = -1
        distance = len(words)
        for index, word in enumerate(words):
            if word == word1:
                wordA = index
            if word == word2:
                wordB = index
            if wordA != -1 and wordB != -1:
                distance = min(abs(int(wordB-wordA)), distance)
        return distance