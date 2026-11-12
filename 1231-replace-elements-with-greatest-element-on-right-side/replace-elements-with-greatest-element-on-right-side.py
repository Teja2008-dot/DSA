class Solution:
    def replaceElements(self, a: list[int]) -> list[int]:
        if not a:
            return a

        max_val = -1

        for i in range(len(a) - 1, -1, -1):
            curr_max = max(max_val, a[i])
            a[i] = max_val
            max_val = curr_max

        return a