class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0], reverse=False)
        answer = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], curr[1])
            else:
                answer.append(curr)
        return answer
