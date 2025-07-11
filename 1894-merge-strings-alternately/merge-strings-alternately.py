class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1,p2=0,0
        merged=[]
        m,n=len(word1),len(word2)

        while p1<m and p2<n:
            merged.append(word1[p1])
            merged.append(word2[p2])
            p1+=1
            p2+=1
        if p1<m:
            merged.append(word1[p1:])
        if p2<n:
            merged.append(word2[p2:])
        return ''.join(merged)


        