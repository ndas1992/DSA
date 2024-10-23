# Search in Rotated Sorted Array
# Asked in companies:Microsoft, Amazon, Uber

def search(nums, target):
    # Implement your solution here
    n = len(nums)-1
    start = 0
    end = n 
    while start<=end:
        mid = (start+end)//2

        if nums[mid]==target:
            print(f'target: {target},    index: {mid}')
            return mid
            
        if nums[start]<=target and target<=nums[mid]:
            end = mid-1
        else:
            start = mid+1
        print(f'start: {start},    end: {end}')
        print('-------------'*5)
    return -1
        

nums = [4, 5, 6, 7, 0, 1, 2]
target = 5
search(nums, target)

nums = [5,1,3]
target = 5
search(nums, target)