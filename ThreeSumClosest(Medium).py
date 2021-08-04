
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum > target:
                    right -= 1
                else:
                    left += 1
            if diff == 0:
                break
        return target - diff