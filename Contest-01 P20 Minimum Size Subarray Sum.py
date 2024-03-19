class Solution(object):
    def minSubArrayLen(self, target, nums):
        j = 0
        _sum = 0
        ans = float('inf')

        check = 0
        for i in range(len(nums)):
            _sum += nums[i]
            while j <= i and _sum >= target:
                check = 1
                ans = min(i - j + 1, ans)
                _sum -= nums[j]
                j += 1

        if check == 0:
            return 0
        return ans
