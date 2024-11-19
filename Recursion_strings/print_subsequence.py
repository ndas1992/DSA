def print_subsequences(s1, takensofar):
    if len(s1)==0 or s1=='':
        print(takensofar)
        return 
    
    print_subsequences(s1[1:], takensofar + s1[0])
    print_subsequences(s1[1:], takensofar)
    
    return

print_subsequences('abc', '')