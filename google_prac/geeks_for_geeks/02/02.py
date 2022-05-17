#https://practice.geeksforgeeks.org/explore?page=1&company[]=Google&sortBy=submissions
#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1/?page=1&company[]=Google&sortBy=submissions#
"""Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
Note: Return -1 if you can't reach the end of the array."""

#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        elem, jumps = 0, 0
        while not elem-1 >= len(arr):
            try:
                elem += arr[elem]
            except IndexError:
                return jumps
            jumps += 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends