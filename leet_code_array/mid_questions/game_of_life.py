#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def liveOrDie(self, board, x, y):
        liveNeb = 0
        if x > 0:
            if board[x-1][y] ==1 or board[x-1][y] == 2 or  board[x-1][y] == 4:
                liveNeb +=1
        if x < len(board) -1:
            if board[x+1][y] ==1 or board[x+1][y] == 2 or  board[x+1][y] == 4:
                liveNeb +=1
        if y > 0:
            if board[x][y-1] ==1 or board[x][y-1] == 2 or  board[x][y-1] == 4:
                liveNeb +=1
        if y < len(board[0]) -1:
            if board[x][y+1] ==1 or board[x][y+1] == 2 or  board[x][y+1] == 4:
                liveNeb += 1
        if x > 0 and y > 0:
            if board[x-1][y-1] ==1 or board[x-1][y-1] == 2 or  board[x-1][y-1] == 4:
                liveNeb += 1
        if x < len(board) -1 and y < len(board[0]) -1:
            if board[x+1][y+1] ==1 or board[x+1][y+1] == 2 or  board[x+1][y+1] == 4:
                liveNeb += 1
        if x < len(board) -1 and y > 0:
            if board[x+1][y-1] ==1 or board[x+1][y-1] == 2 or  board[x+1][y-1] == 4:
                liveNeb += 1
        if x > 0 and y < len(board[0]) -1:
            if board[x-1][y+1] ==1 or board[x-1][y+1] == 2 or  board[x-1][y+1] == 4:
                liveNeb += 1
        if board[x][y] == 1:
            if liveNeb == 2 or liveNeb ==3:
                return 4
            else:
                return 2
        else:
            if liveNeb == 3:
                return 3
            else:
                return 5




    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # if the cell is current live and should die in this step
        livshouldDie = 2
        # if the cell is current die and should live in this step
        dieShouldLive = 3
        liveShouldLive = 4
        dieShouldDie = 5
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = self.liveOrDie(board, x, y)
        print(board)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 2 or board[x][y] == 5:
                    board[x][y] = 0
                elif board[x][y] == 3 or board[x][y] == 4:
                    board[x][y] = 1
