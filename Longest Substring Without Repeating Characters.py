class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        answer = float('-inf')
        for i in range(0, len(s) - 1):
            d = {s[i]: i}
            x = i + 1
            while x != len(s) - 1 and s[x] not in d.keys():
                d[s[x]] = x
                x += 1
            if x == len(s) - 1 and s[x] not in d.keys():
                answer = max(answer, (x - i) + 1)
            else:
                answer = max(answer, x - i)
        return answer
