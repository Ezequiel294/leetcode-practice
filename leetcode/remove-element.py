class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        for i in range(length):
            if nums[i - k] == val:
                nums.pop(i - k)
                k += 1

        return length - k
