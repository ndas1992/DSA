def palindrome(s1):
    if len(s1)==0 or s1=='':
        return True
    
    s = 0
    e = len(s1)
    small_ans = palindrome(s1[s+1:e-1])

    if small_ans == True:
        if s1[0] == s1[-1]:
            return True
    else:
        return False




print(palindrome('nayan'))