class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        copy = []
        for i in range(len(nums)):
            copy.append(nums[i])

        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = copy[i]
