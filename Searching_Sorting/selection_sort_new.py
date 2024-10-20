def selection_sort(lst):
    n = len(lst)
    temp_list = lst
    print(lst)
    for pas in range(n):
        temp_min = min(temp_list) #11
        index_to_exchange = lst.index(temp_min)
        value_to_exchange = temp_list[0]

        lst[pas] = temp_min
        lst[index_to_exchange] = value_to_exchange

        temp_list = lst[pas+1:]

    print(f'Sorted list: {lst}')



lst = [12, 45, 10, 6, 98, 56, 28, 99, 145]
selection_sort(lst)