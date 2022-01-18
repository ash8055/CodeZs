def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    k = s[0] 
    s[0] = s[-1] 
    s[-1] = k 
    for i in range(1,len(s)//2):
        k = s[i] 
        s[i] = s[-(i+1)] 
        s[-(i+1)] = k 
