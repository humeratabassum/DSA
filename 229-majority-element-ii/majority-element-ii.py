class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        #first find 2 candidates
        count1,count2=0,0
        cand1=cand2=None

        for num in nums:
            if num==cand1:
                count1+=1
            elif num==cand2:
                count2+=1
            elif count1==0:
                cand1,count1=num,1
            elif count2==0:
                cand2,count2=num,1
            else:
                count1-=1
                count2-=1
        result=[]
        n=len(nums)
        if nums.count(cand1) > n // 3:
            result.append(cand1)
        if cand2 != cand1 and nums.count(cand2) > n // 3:
            result.append(cand2)
        
        return result





#solution 2
"""
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Create a Counter to store the count of each element
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements

"""