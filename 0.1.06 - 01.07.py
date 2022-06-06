"""  01.06. Compress String LCCI
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).

it is easy to solve but actually there something worth to pay attention!
in python the string is a "immutable" variable, other immutable object types are: int，string，float，tuple ; mutable object types are: list，dictionary.
The immutable object we can take it as the parameter transfer using the value, 
while this parameter using the pointer to transfer (IN C program language way to understand)
"""
def compressString(self, S: str) -> str:
    if not S:
        return ""
    n = len(S)
    temp = S[0]
    k = 0
    ans = ""
    for i in range(n):
        if S[i]==temp:
            k+=1
        else:
            ans = ans + temp +str(k)   #so this concatenating strings way is kind of costy
            temp = S[i]
            k = 1
    ans = ans + temp +str(k)
    if len(ans)>=n:
        return S
    else:
        return ans
      
#here is the code using two pointer and the list as res (better than string)
def compressString1(self, S: str) -> str:
    i, j, ls = 0, 0, len(S)
    res = []
    while i < ls:
        while j < ls and S[i] == S[j]:
            j += 1
        res.append(S[i])
        res.append(str(j - i))
        i = j
    res = ''.join(res)
    return res if len(res) < ls else S


