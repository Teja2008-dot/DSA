class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        start = 0
        result = 0 if 0 in nums else float('-inf')

        negatives = 0
        first = 0
        last = 0

        nums.append(0)
        for i, x in enumerate(nums):
            # Track negatives
            if x < 0:
                if negatives == 0:
                    first = last = i
                else:
                    last = i
                negatives += 1
            if x != 0:
                continue
            if start == i:
                start += 1
                continue

            result = max(
                result,
                nums[start] if i - start == 1 else 
                prod(nums[start:i]) if negatives % 2 == 0 else max(
                    prod(nums[first+1:i]), prod(nums[start:last])
                )
            )
            start = i + 1
            negatives = 0

        return result