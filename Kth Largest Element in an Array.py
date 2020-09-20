import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        answer = nums[0]
        for i in range(0, k):
            answer = heapq.heappop(heap)
        return -answer
