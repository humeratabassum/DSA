class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:(p[0],-p[1]))

        ans=0
        n=len(points)

        for i in range(n):
            y_i=points[i][1]
            max_y_seen=-10**9

            for j in range(i+1,n):
                y_j=points[j][1]

                if y_j <= y_i and y_j > max_y_seen:
                    ans+=1
                    max_y_seen=y_j
        return ans
        