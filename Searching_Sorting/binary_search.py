def binary_search(arr, target):
    size = len(arr)
    start = 0
    end = size-1
    
    while start <= end:
        mid = (end + start)//2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
    
    return -1

my_list = [10,23,35,45,50,70,85]
target = 85

result = binary_search(my_list, target)
print(result)