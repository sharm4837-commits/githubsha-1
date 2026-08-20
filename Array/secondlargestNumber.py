class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        second = -1

        for i in range(1, len(nums)):
            if nums[i] > largest:
                second = largest
                largest = nums[i]

            elif nums[i] < largest and nums[i] > second:
                second = nums[i]

        return second
