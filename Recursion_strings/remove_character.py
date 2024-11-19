def remove_character(s1, ch):
    if len(s1)==0 or s1=='':
        return s1
    
    small_ans = remove_character(s1[1:], ch)

    if s1[0]==ch:
        return small_ans
    else:
        return s1[0] + small_ans

    
print(remove_character('abzczz', 'z'))