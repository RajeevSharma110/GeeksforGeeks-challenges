#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 23:24:21 2021

@author: Rajeev
"""


class Solution:
    def removeDups(self, S):
        j=""
        for i in range(len(S)):
            if S[i] not in j:
                j=j+S[i] # code here
        return j
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s = input()
        
        ob = Solution()    
        answer = ob.removeDups(s)
        
        print(answer)


# } Driver Code Ends