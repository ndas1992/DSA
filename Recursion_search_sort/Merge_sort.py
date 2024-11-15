def Merge(arr, s, m, e):
    i = s
    j = m+1
    output = []

    while i<=m and j<=e:
        if arr[i] < arr[j]:
            output.append(arr[i])
            i = i+1
        elif arr[i] > arr[j]:
            output.append(arr[j])
            j = j+1
        elif arr[i] == arr[j]:
            output.append(arr[i])
            output.append(arr[j])
            i = i+1
            j = j+1
    while i<=m:
        output.append(arr[i])
        i = i+1
    while j<=e:
        output.append(arr[j])
        j = j+1

    start_arr = s
    start_op = 0
    while start_arr<=e:
        arr[start_arr] = output[start_op]
        start_arr = start_arr+1
        start_op = start_op+1

    return arr

def Merge_sort_helper(arr, s, e):
    if s>=e:
        return
    
    m = (e+s)//2

    Merge_sort_helper(arr, s, m)
    Merge_sort_helper(arr, m+1, e)
    
    return Merge(arr, s, m, e)

def Merge_sort(arr):
    s = 0
    e = len(arr)-1
    return Merge_sort_helper(arr, s, e)

    
arr = [3,2,5,2,8,2,1]
print(Merge_sort(arr))