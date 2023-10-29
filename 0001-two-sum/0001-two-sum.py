class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        result = []
        for i in range(length - 1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    result = [i,j]
        return result
        