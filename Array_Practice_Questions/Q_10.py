def maxSubArray(nums):
        cur_sum = 0
        if len(arr)>0:
            max_sum = nums[0]
        else:
             max_sum = 0
        for i in nums:
            cur_sum = cur_sum + i
            print(f'cur_sum: {cur_sum},   max_sum: {max_sum}')
            max_sum = max(max_sum, cur_sum)
            if cur_sum<0:
                cur_sum = 0
            print(f'cur_sum: {cur_sum},   max_sum: {max_sum}')
            print('----------'*5)
        print(max_sum)
        return max_sum


arr = []
maxSubArray(arr)       