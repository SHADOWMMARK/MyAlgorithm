# 01.02. Check Permutation LCCI  Given two strings,write a method to decide if one is a permutation of the other.
# also can use the hash table to count the letters occurance number
def CheckPermutation(self, s1: str, s2: str) -> bool:
    a = list(s1)
    b = list(s2)
    a.sort()
    b.sort()
    return a==b

      
#01.03. String to URL LCCI
"""Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array 
so that you can perform this operation in place.

Because, there is plenty space in the string so it is also right to just replace directly in the original S string
"""
def replaceSpaces(self, S: str, length: int) -> str:
    hel = S.split(" ")
    ans = ''
    k = length
    for item in hel:
        ans += item
        k -= len(item)
        if k > 0:
            ans += '%20'
            k -= 1
        else: break
    return ans
