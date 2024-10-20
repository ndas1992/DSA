def selection_sort(lst):
    # Your code goes here
    print(lst)
    n = len(lst)
    for pas in range(n-1):
        print(pas)
        min_index = pas
        for i in range(pas, n):
            if lst[i] < lst[min_index]:
                min_index = i
                print(f'min_index: {i}')

        lst[pas], lst[min_index] = lst[min_index], lst[pas]
        print(lst)
    
    
lst = [64, 25, 12, 22, 11]
selection_sort(lst)