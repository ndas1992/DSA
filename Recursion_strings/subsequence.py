def subsequences(s1):
    if len(s1)==0 or s1=='':
        return ['']
    
    small_ans = subsequences(s1[1:])
    small_list = []
    for i in small_ans:
        small_list.append(s1[0]+i)
    return small_ans + small_list


print(subsequences('abc'))



    