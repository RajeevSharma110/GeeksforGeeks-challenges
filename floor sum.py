#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 00:30:37 2021

@author: Rajeev
"""

#User function Template for python3

class Solution:
	def sumofproduct(self, n):
		ans=0
		for i in range(1,n+1):
		    ans+=(i*(n//i))
		return ans
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.sumofproduct(n)
		print(ans)
# } Driver Code Ends