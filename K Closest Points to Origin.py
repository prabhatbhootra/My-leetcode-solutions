import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        answer = []
        heap = [((point[0]**2+point[1]**2), point) for point in points]
        heapq.heapify(heap)
        for i in range(0, K):
            answer.append(heapq.heappop(heap)[1])
        return answer
