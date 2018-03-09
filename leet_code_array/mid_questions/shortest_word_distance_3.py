class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        curcount = 0
        word1index = -1
        word2index = -1
        mincount = len(words)
        for index, word in enumerate(words):
            if word1 != word2:
                if word == word1:
                    word1index = index
                    if word2index >=0 and word1index >=0:
                        curcount = abs(word2index - word1index)
                        if curcount < mincount:
                            mincount = curcount
                if word == word2:
                    word2index = index
                    if word2index >= 0 and word1index >=0:
                        curcount = abs(word2index - word1index)
                        if curcount < mincount:
                            mincount = curcount
            else:
                if word == word2:
                    if word2index >= 0:
                        curcount = abs(word2index - index)
                        if curcount < mincount:
                            mincount = curcount
                    word2index = index
        return mincount



        