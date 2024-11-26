import re
import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned = cleaned.lower()
        l=0
        r=len(cleaned)-1
        palindrome=True
        while(l<math.ceil(0.5*len(cleaned)) and l!=r):
            if(cleaned[l]==cleaned[r]):
                palindrome=True
            else:
                palindrome=False
                break
            l+=1
            r-=1
        return palindrome
start=True
while(start):
    sol=Solution()
    user_input=input("Enter palindrome checking string:\n")
    result=sol.isPalindrome(user_input)
    if(result==False):
        print("Not a palindrome")
    else:
        print("It is a palindrome")