class Solution(object):
    def beautySum(self, s):
        total_beauty=0
        
        n=len(s)

        for i in range(n):
            freq={}

            for j in range(i,n):
                if s[j] in freq:
                    freq[s[j]]+=1
                else:
                    freq[s[j]]=1
                max_freq=max(freq.values())
                min_freq=min(freq.values())

                total_beauty+=(max_freq-min_freq)
        return total_beauty

        """
        :type s: str
        :rtype: int
        """
        