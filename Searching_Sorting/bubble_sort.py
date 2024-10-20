def bubble_sort(lst):
    # Your code goes here
    n = len(lst)
    for pas in range(n-1):
        print(f"{pas} pass")
        for i in range(n-1-pas):
            print(lst[i],'----', lst[i+1])
            if lst[i] >lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]    
            print(lst)
    print(f"Sorted List: {lst}")
    return lst
              
lst = [8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(lst)