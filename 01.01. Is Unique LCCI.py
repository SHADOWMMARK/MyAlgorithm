""" this prob bring the idea that using a int or a number to replace an array to record the char that if it has occured or not!

prob statment:
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?

idea is using a 26-bit int to stand for 26 small letters in English, using the << operate to change the "distance" between them
"""

class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        n = len(astr)
        if n>26: return False  #if a astr is longer than 26 then it must have same letters
        for i in range(n):
            moveBit = ord(astr[i])-ord("a")
            if mark & (1<<moveBit)!=0:
                return False
            else:
                mark = mark|(1<<moveBit)
        return True
