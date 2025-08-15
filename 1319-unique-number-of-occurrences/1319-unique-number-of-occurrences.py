from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=Counter(arr)
        return len(count.values())==len(set(count.values()))





        # freq={}

        # for num in arr:
        #     freq[num]=freq.get(num,0)+1
        
        # counts=list(freq.values())

        # return len(counts)==len(set(counts))

        