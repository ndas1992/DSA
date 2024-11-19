def print_permutations(s1, takensofar):
    if len(s1)==0 or s1=='':
        print(takensofar)
        return
    
    for i in range(0, len(takensofar)+1):
        print_permutations(s1[1:], takensofar[0:i] + s1[0] + takensofar[i:])
        # print(s1[1:], takensofar[0:i] + s1[0] + takensofar[i:])
    return

print_permutations('abc', '')
