class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        #initialize an empty list of 100 elements
        arr = ['']*100
        pre=0
        cur=1
        nex=1
        total=n
        while n>0:
            arr[total-n]=cur
            pre=cur
            cur=nex
            nex=pre+cur
            n=n-1
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
