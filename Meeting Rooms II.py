class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        startTimes = sorted([interval[0] for interval in intervals], key=lambda x: x, reverse=False)
        endTimes = sorted([interval[1] for interval in intervals], key=lambda x: x, reverse=False)
        startpoint = 0
        endpoint = 0
        while startpoint < len(intervals):
            if startTimes[startpoint] >= endTimes[endpoint]:
                rooms -= 1
                endpoint += 1
            rooms += 1
            startpoint += 1
        return rooms
