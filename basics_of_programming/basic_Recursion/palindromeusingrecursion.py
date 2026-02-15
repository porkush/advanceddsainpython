def palire(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return palire(s,l+1,r-1)

s="aabbbbbaa"
print(palire(s,0,len(s)-1))