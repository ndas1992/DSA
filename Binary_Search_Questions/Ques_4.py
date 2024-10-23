# Minimum in Rotated Sorted Array
# Asked in companies: Google, Arcesium, Phone Pe, Qualcomm

def findMin(nums):
    n = len(nums)-1
    start = 0
    end = n
    print(nums)
    while start<=end:
        print('--------------'*5)
        mid = (start+end)//2
        mid_left = mid-1
        mid_right = mid+1
        print(f'start: {start},    end: {end},   mid: {mid}')
        if start==end:
            return nums[0]
        print(f'mid_left: {nums[mid_left]},    mid: {nums[mid]},    mid_right: {nums[mid_right]}')
        if (nums[mid_left]<nums[mid]) and (nums[mid]<nums[mid_right]):
            start = mid+1
        elif (nums[mid_left]>nums[mid]):
            print(f'nums_mid_right: {nums[mid]}')
            return nums[mid]
        elif (nums[mid]>nums[mid_right]):
            print(f'nums_mid_right: {nums[mid_right]}')
            return nums[mid_right]
        print(f'start: {start},    end: {end}')
        print(f'arr: {nums[start: end+1]}')
    return 0

nums = [4, 5, 6] 
output = findMin(nums)
print(output)
