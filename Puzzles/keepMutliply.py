"""
. Keep Multiplying Found Values by Two

You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.]
    """
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        matched=True
        while (matched):
            if original in nums:
                original = original*2
                matched=True
            else:
                matched=False
        return original
        

if __name__ == '__main__':
    obj = Solution()
    print(obj.findFinalValue([5,3,6,1,12],3))