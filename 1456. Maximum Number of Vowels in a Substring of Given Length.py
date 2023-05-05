
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o','u'}
    ans = 0
    temp = 0
    l, r = 0, k
    for i in s[l:r]:
        if i in vowels:
            temp += 1
    ans = temp
    while r<len(s):
        otp,inp = s[l],s[r]
        if (otp not in vowels) and (inp in vowels):
            temp += 1
        elif (otp in vowels) and (inp not in vowels):
            temp -= 1
        l+=1
        r+=1
        ans = max(ans,temp)
    return ans
