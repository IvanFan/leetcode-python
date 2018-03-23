#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def detectWord(self, wordList, board, x, y, wordIndex):
        if wordIndex == len(wordList) -1 and board[x][y] == wordList[wordIndex]:
            return True
        if board[x][y] != wordList[wordIndex]:
            return False
        else:
            wordIndex += 1
            tem = board[x][y]
            board[x][y] = ''
           # up
            if x>0:
                if self.detectWord(wordList, board, x-1, y, wordIndex) == True:
                   return True
           # down
            if x < len(board) -1:
                if self.detectWord(wordList, board, x+1, y, wordIndex) == True:
                   return True
            if y > 0:
                if self.detectWord(wordList, board, x, y-1, wordIndex) == True:
                    return True
            if y < len(board[0]) -1:
                if self.detectWord(wordList, board, x, y+1, wordIndex) == True:
                    return True
            board[x][y] = tem
            return False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        wordList = list(word)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.detectWord(wordList, board, x, y, 0) == True:
                    return True
        return False
