
# Find First and Last Position of Element in Sorted Array
# Asked in companies: Goldman sachs, Amazon, Wipro, Airtel
def binsearch(nums, target, leftBias):
    n = len(nums)
    start = 0
    end = n-1
    index = -1
    while start<=end:
        mid = (start+end)//2
        if nums[mid]>target:
            end = mid-1
        elif nums[mid]<target:
            start = mid+1
        else:
            index = mid
            if leftBias:
                end = mid-1
            else:
                start = mid+1
    return index

def searchRange(nums, target):
    start = binsearch(nums, target, True)
    end = binsearch(nums, target, False)
    return [start, end]

    
nums = [5, 6, 6, 6, 6, 7, 7, 8, 8, 10]
target = 7
arr = searchRange(nums, target)
print(arr)