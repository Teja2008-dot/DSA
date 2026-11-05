class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        max_freq = 0
        nums.sort()
        count = 0
        freq = 0
        for i in range(len(nums)):
            count += nums[i]
            freq += 1
            if nums[i]*freq - count > k :
                freq -= 1
                count -= nums[i-freq]
            max_freq = max(max_freq, freq)

        return max_freq

        