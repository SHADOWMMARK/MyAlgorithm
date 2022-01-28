class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(s):
            if not "#" in s:
                return s
            r = s.rfind("#")
            s = list(s)
            temp = 0
            while r >= 0:
                if s[r]!="#" and temp>0:
                    s[r]=""
                    temp-=1
                if s[r]=="#":
                    temp+=1
                r-=1
            while "#" in s:
                s.remove("#")
            return "".join(s)
        return back(s)==back(t)
