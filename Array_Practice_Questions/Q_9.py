def move_zeroes(nums):
    n = len(nums)
    print(nums)
    j = 0
    for i in range(n):
        print(f'(i, j): ({i}, {j}),     num[i]: {nums[i]},    num[j]: {nums[j]}')
        if nums[i] != 0 and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            print(f'condition satisfied: {nums}')
        if nums[j] != 0:
            j = j + 1
            print(f'j is incremented as nums[j] (nums[{j}])!=0')
        print(f'incremental num: {nums}')
        print('-----------------'*6)
    print(nums)

nums = [0, 1, 0, 3, 12]
move_zeroes(nums)