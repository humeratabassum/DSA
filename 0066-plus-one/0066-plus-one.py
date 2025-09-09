class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

    # Step 1: Convert list of digits into a string
        n="".join(map(str,digits))
    
        num=int(n)
        num+=1
        s_new=str(num)
        result=[int(char) for char in s_new]
        return result




        # num=int("".join(map(str,digits)))
        # num+=1
        # return [int(d) for d in str(num)]
       