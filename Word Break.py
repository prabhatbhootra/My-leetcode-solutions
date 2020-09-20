class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {}
        wordSet = set(wordDict)
        def helper(sub: str) -> bool:
            if sub in d:
                return d[sub]
            elif sub in wordSet:
                return True
            else:
                d[sub] = False
            for i in range(0, len(sub)):
                if sub[0:i+1] in d:
                    if d[sub[0:i+1]] == True and helper(sub[i+1:]) == True:
                        return True
                elif sub[0:i+1] in wordSet:
                    d[sub[0:i+1]] = True
                    if helper(sub[i+1:]) == True:
                        return True
                else:
                    d[sub[0:i+1]] = False
        if helper(s) == True:
            return True
        return False
