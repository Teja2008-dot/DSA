class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        sset=set(nums)
        nums[:]=sorted(sset)
        return len(sset)