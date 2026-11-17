class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        while s:
            val = s.pop()
            curr = 1
            prev, nxt = val - 1, val + 1
            while prev in s:
                curr += 1
                s.remove(prev)
                prev -= 1          
            
            while nxt in s:
                curr += 1
                s.remove(nxt) 
                nxt += 1          
            ans = max(ans, curr)
        return ans