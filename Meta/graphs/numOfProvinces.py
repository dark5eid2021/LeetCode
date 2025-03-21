from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)
    
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i)


        return provinces









"""
There are n cities. Some of them are connected, while some are not.
 If city a is connected directly with city b, and city b is connected directly with city c, 
 then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and 
no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city
 and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


"""