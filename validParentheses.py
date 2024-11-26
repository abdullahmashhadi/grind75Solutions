class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapClose={')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapClose:
                if stack and stack[-1]==mapClose[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
start=True
while(start):
    sol=Solution()
    user_input=input("Enter parentheses checking string:\n")
    result=sol.isValid(user_input)
    if(result==False):
        print("Not a valid parentheses combination")
    else:
        print("It is a valid parentheses combination")