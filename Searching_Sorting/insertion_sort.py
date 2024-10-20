def insertion_sort(lst):
    # Your code goes here
    n = len(lst)
    for pas in range(1, n):
        ele = lst[pas]
        print(f'pas: {pas}     element: {ele}')
        for i in range(pas):
            temp_ele = lst[pas-i-1]
            print(f'element: {ele},   temp_element: {temp_ele}')
            if ele < temp_ele:
                print('satisfied')
                lst[pas-i-1], lst[pas-i] = lst[pas-i], lst[pas-i-1]
            else:
                print('already sorted')
                print(f'lst:   {lst}')
                break
            print(f"Lst: {lst}")
        print(i, '------------------'*5)
    return lst

lst = [12, 25, 11, 34, 90, 22]
insertion_sort(lst)