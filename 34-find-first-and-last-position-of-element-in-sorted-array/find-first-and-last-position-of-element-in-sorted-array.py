class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def FirstOccurence():
            ans=-1
            low=0
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        def LastOccurence():
            ans=-1
            low=0
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        return [FirstOccurence(),LastOccurence()]                                


        