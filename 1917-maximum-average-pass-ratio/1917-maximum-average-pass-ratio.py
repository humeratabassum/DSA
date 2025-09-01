import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p,t):
            return (p+1)/(t+1)-p/t      #new ratio - old ratio

        heap=[(-gain(p,t),p,t) for p,t in classes]
        heapq.heapify(heap)     

        for _ in range(extraStudents):
            g,p,t=heapq.heappop(heap)
            p+=1
            t+=1

            heapq.heappush(heap,(-gain(p,t),p,t))

        total_ratio=0
        for _ , p ,t in heap:
            total_ratio+=p/t
        return total_ratio/len(classes)
