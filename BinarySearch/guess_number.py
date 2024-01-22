# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import math


class Solution:
    def guess(self, min:int, max: int, pick: int) -> int:
            # convert float to int
            mid =  (min + max) // 2
            if mid == pick:
                return 0
            if mid < pick:                
                return self.guess(mid, max, pick)
            if mid > pick:
                return self.guess(min, mid, pick)
            return -1
            
    def guessNumber(self, n: int) -> int:
        return self.guess(1, 10, n)
    
solution = Solution()
solution.guessNumber(6)