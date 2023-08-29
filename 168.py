ans = ""
columnNumber = 943566
ans = chr(ord('A')+(columnNumber-1) % 26)
while columnNumber > 26:
    if ans[-1] == 'Z': # idk how i pass last time, but this is wrong: it should check last time's character if it is Z or not
                        # but here is always checking the end of the ans
        columnNumber -= 26
    columnNumber  //= 26
    k = (columnNumber - 1)%26
    ans = chr(ord('A')+(k)) + ans
    
print( ans )