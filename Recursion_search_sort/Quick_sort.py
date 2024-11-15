def partition_function(arr, s, e):
    pivot = s

    for i in range(s, e):
        if arr[i]<arr[e]:
            pivot = pivot+1
    arr[pivot], arr[e] = arr[e], arr[pivot]

    i = s
    j = e
    while i<pivot or j>pivot:

        if arr[i]<= arr[pivot]:
            i = i+1
        elif arr[j]>= arr[pivot]:
            j = j-1
        # elif arr[i]>arr[pivot] and arr[j]<arr[pivot]:
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1
    return pivot



def Quick_sort(arr, s, e):
    if s>=e:
        return
    pivot_index = partition_function(arr, s, e)

    Quick_sort(arr, s, pivot_index-1)
    Quick_sort(arr, pivot_index+1, e)
    return

arr = [3,6,7,2,1,4,5,4, 10]
Quick_sort(arr, 0, len(arr)-1)
print(arr)

