class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        num = 
        start = search(num,target,True)
        end = search(num,target,False)
        ans[0] = start
        ans[1] = end
        return ans
    def search(num,target,first):
        ans = -1
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = start + (end-start)/2
            if(target == nums[mid]):
                ans = mid
                if(first):
                    mid = end -1
                else:
                    mid = start + 1
            if(target < nums[mid]):
                end = mid -1
            else:
                start = mid+1
        return ans    
