def permutation(s1):
    if s1=='' or len(s1)==0:#base case
        return ['']
    
    small_ans = permutation(s1[1:]) #['bc', 'cb']
    all_ans = []
    for perm in small_ans:
        for i in range(0, len(perm)+1):
            all_ans.append(perm[0:i] + s1[0] + perm[i:] )
            print(f's1: {s1}, small_ans: {small_ans}, perm: {perm}, all_ans: {all_ans}')
        print('======='*4)
    print('-------------'*2)
    return all_ans

print(permutation('abc'))
    

    