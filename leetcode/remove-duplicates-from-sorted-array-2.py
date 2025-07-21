class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        unique = [nums[0], nums[1]]

        i = 2
        while i < len(nums):
            if nums[i] not in unique:
                unique.append(nums[i])
            else:
                if unique[len(unique) - 2] != nums[i]:
                    unique.append(nums[i])
            i += 1

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)
