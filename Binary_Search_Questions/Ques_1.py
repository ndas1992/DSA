# Count negative numbers in a sorted matrix
# Asked in companies: Samsung, Oyo, Groww, Dell

def countNegatives(grid):
    # Implement your solution here
    count = 0
    for arr in grid:
        start = 0
        end = len(arr)-1
        print(arr)
        while start <= end:
            mid = (end+start)//2
            print(f'start: {start},   end: {end},    mid: {mid}')
            if arr[mid] < 0:
                end = mid - 1
            elif arr[mid] >= 0:
                start = mid + 1
            print(f'start: {start},   end: {end},    mid: {mid}')
            print('--------------------'*3)
        count = count + len(arr[end+1:])
        print(f'{count} = {count} + {len(arr[mid+1:])}')
        print(f'count = count + len({arr[mid+1:]})')
        print(count)
            
        print('--------------------'*3)
    return count

grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
countNegatives(grid)
