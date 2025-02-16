class Solution(object):
    def twoSum(self, numbers, target):
        low,high=0,len(numbers)-1
        while low<high:
            curr_sum=numbers[low]+numbers[high]

            if curr_sum==target:
                return [low+1,high+1]
            elif curr_sum<target:
                low+=1
            else:
                high-=1
        return []
                
        