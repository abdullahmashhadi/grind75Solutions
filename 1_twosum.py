from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        output=[]
        for i in range (len(nums)):
            if target-nums[i] in hashmap:
                output.append(i)
                output.append(hashmap[target - nums[i]])
            else:
                hashmap[nums[i]]=i
        return output
start=True
while(start):
    sol=Solution()
    array = list(map(int, input("Enter array separated by spaces:\n").split()))
    target=int(input("Enter your target?\n"))
    result=sol.twoSum(array,target)
    print(result)