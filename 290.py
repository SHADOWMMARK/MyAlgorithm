class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split(" ")
        if len(words)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            else:
                 d[pattern[i]] = words[i]
        return True and len(d.values()) == len(set(d.values()))