from fractions import gcd
class Solution(object):
    def findGCD(self, nums):
        mx,mn=max(nums),min(nums)
        return gcd(mn,mx)
        
        