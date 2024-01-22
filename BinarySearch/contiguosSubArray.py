class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       l = 0
       r = 0
       sum = 0
       while r < n:
           
        sum += arr[r]
        if sum == s:
            return [l+1, r+1]
        elif sum > s:
            sum = sum - arr[l]
            l+= 1
            if sum == s:
                return [l+1, r+1]
        r += 1  
       return [-1]
   
sol = Solution()
op = sol.subArraySum([1,2,3,7,5], 5, 12)
print(op)