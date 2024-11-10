def power2(n):
    if n==1:
        return 2
    ans = 2*power2(n-1)
    return ans

print(power2(5))