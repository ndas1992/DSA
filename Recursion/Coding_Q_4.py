def number_of_digits(n):
    if n>=1 and n<=9:
        return 1
    elif n==0:
        return 1
    small_number = int(n/10)
    small_ans = number_of_digits(small_number)
    ans = small_ans + 1
    return ans

print(number_of_digits(000))
print(number_of_digits(65484258))