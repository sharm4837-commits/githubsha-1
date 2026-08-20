class Solution:
    def countFrequencies(self, nums):
        n = len(nums)
        visited = [False] * n
        result = []

        for i in range(n):
            if visited[i]:
                continue

            count = 0

            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
                    visited[j] = True

            result.append([nums[i], count])

        return result
