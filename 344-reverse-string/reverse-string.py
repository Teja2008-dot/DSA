class Solution:
    def reverseString(self, s: list[str]) -> None:
        i=0
        j=len(s)-1
        while(True):
            s[j],s[i]=s[i],s[j]
            i+=1
            j-=1
            if(i>=j):
                break
        