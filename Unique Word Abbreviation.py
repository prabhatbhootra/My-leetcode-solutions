class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = {}
        for w in dictionary:
            ab = w
            if len(w) > 2:
                ab = w[0] + str(len(w) - 2) + w[-1]
            if ab not in self.d.keys():
                self.d[ab] = set([w])
            else:
                if w not in self.d[ab]:
                    self.d[ab].add(w)

    def isUnique(self, word: str) -> bool:
        abr = word
        if len(word) > 2:
            abr = word[0] + str(len(word) - 2) + word[-1]
        if abr not in self.d.keys():
            return True
        else:
            if len(self.d[abr]) == 1 and word in self.d[abr]:
                return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
