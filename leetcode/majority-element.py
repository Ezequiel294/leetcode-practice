class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        most = nums[0]
        count = 1
        count_other = 0
        for i in range(1, len(nums)):
            if most == nums[i]:
                count += 1
            else:
                count_other += 1
                if count_other > count:
                    most = nums[i]
                    count = count_other
                    count_other = 0

        return most
