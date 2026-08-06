class Solution:
    def reverse(self, arr: list, n: int) -> None:
        
        self.helper(arr, 0, n - 1)
    
    def helper(self, arr, left, right):

        if left >= right:
            return
        
        
        arr[left], arr[right] = arr[right], arr[left]
        self.helper(arr, left + 1, right - 1)
