##problem statement:
#Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# the first thing comes to my mind to solve this problem is to use the stack like the classical problem sloving the  "(" and ")", when left ")" occurs,
# put )into the stack and the thing until a ( occur then delete all the thing between the ( ) and the (). 
# this problem can also be solved using stack but using the pointer can save a lot running space:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(s):    #because dealing the same options to both strings so create a function to run two times
            if not "#" in s:
                return s
            r = s.rfind("#")    #set a pointer by finding the leftmost "#"
            s = list(s)
            temp = 0
            while r >= 0:
                if s[r]!="#" and temp>0:    #if the pointer is not # and temp != 0 (means on the right of the pointer there is #), so delete the pointer's content
                    s[r]=""
                    temp-=1
                if s[r]=="#":           #if the pointer is # temp plus 1
                    temp+=1
                r-=1
            while "#" in s:             # in case there is useless # at front of the str, remove them
                s.remove("#")
            return "".join(s)
        return back(s)==back(t)
