def reversePrefix(self, word: str, ch: str) -> str:
    if ch not in word:
        return word
    ch_idx = word.index(ch)
    ans = word[:ch_idx+1]
    return ans[::-1]+word[ch_idx+1:]
