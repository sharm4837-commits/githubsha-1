class Solution:
    def mostFrequentElement(self, nums):
        n = len(nums)
        max_count = 0
        answer = 0

        for i in range(n):
            count = 0

            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1

            if count > max_count:
                max_count = count
                answer = nums[i]

            elif count == max_count:
                if nums[i] < answer:
                    answer = nums[i]

        return answer
