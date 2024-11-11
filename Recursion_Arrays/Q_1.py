def sum_array_head(l):
    if len(l)==0:
        return 0
    # if len(l)==1:
    #     return l[0]
    
    sum = l[0] + sum_array_head(l[1:]) 

    return sum

print(sum_array_head([2,3,4,5]))




def sum_array_tail(l, sum=0):
    if len(l)==0:
        return sum
    
    sum = l[0] + sum
    return sum_array_tail(l[1:], sum)

print(sum_array_tail([2,3,4]))

