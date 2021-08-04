class Solution:
    def threeSum(nums):
        nums.sort()
        triplets = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1

        return list(triplets)