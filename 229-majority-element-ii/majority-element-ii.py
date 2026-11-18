class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        h={}
        n1=len(nums)//3
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        l=[]
        for i in h:
            if h[i]>n1:
                l.append(i)
        return l