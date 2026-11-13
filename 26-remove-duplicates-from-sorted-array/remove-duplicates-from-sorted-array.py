class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new = sorted(list(set(nums)))
        nums.clear()
        nums.extend(new)
        return len(nums)
        