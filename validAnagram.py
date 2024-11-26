class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        s_freq=self.calcFrequency(s)
        t_freq=self.calcFrequency(t)
        return s_freq==t_freq
        
    def calcFrequency(self,s):
        c_freq={}
        for c in s:
            if c in c_freq:
                c_freq[c]+=1
            else:
                c_freq[c]=1
        return c_freq
start=True
while(start):
    sol=Solution()
    s=input("Enter first string:\n")
    t=input("Enter second string:\n")
    result=sol.isAnagram(s,t)
    if(result==False):
        print("not anagram")
    else:
        print("It is anagram")