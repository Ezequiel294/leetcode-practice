class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # key point are the zero's
        zeros = [i for i, x in enumerate(nums) if x == 0]

        # Last index zero doesn't affect
        if (len(zeros) > 0) and (zeros[-1] == (len(nums) - 1)):
            zeros.pop()

        # if no zero's, can always reach the end
        if len(zeros) == 0:
            return True

        for i in range(len(zeros) - 1, -1, -1):
            passes = 0
            for j in range(zeros[i] - 1, -1, -1):
                if nums[j] > (zeros[i] - j):
                    passes = 1
                    continue
            if passes == 0:
                return False

        return True
