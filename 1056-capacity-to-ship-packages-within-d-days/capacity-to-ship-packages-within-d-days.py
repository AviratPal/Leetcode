class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=high
        while low<=high:
            mid=(low+high)//2
            days_used=1
            current=0
            for i in weights:
                if current+i<=mid:
                    current+=i
                else:
                    days_used+=1
                    current=i
            if days_used<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans            
                        

        

        