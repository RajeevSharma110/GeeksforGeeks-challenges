#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:10:03 2021

@author: Rajeev
"""


class Solution:
    def oppositeFaceOfDice(self, N):
        if N==1:
            return 6
        elif N==2:
            return 5
        elif N==3:
            return 4
        elif N==4:
            return 3
        elif N==5:
            return 2
        elif N==6:
            return 1
        #code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends