class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_water=0

        while l<r:
            h=min(height[l],height[r])           #find min height so it doesnt overflow
            w=r-l                                #width = left-right 
            area=h*w                               #calculate area
            max_water=max(max_water,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_water
        