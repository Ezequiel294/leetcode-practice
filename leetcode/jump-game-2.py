class Solution(object):
    def jump(self, nums):
        min_jumps = 0

        i = 0
        while i < len(nums) - 1:
            # Calculate what the maximum jump is from this index
            if (nums[i] + i >= len(nums) - 1):
                return min_jumps + 1
            else:
                max_jump = nums[i] + i

            # Find the best jump from the current index
            best_distance = 0
            for j in range(i + 1, max_jump + 1):
                if (nums[j] == 0) or ((nums[j] + j) < best_distance):
                    continue

                best_distance = nums[j] + j
                index_distance = j

            min_jumps += 1
            i = index_distance

        return min_jumps
