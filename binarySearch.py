from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        while(left<=right):
            mid=int((left+right)/2)
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return -1
start=True
while(start):
    sol=Solution()
    array=list(map(int,input("Enter sorted array (space-separated):\n").split()))
    target=int(input("Enter the element you want to find in the array:\n"))
    result=sol.search(array,target)
    print(result)                