class Solution:
    def reverseNumber(self, n):
        reverse = 0
        while n > 0:
            last_digit = n % 10
            reverse = (reverse * 10)+ last_digit
            n = n//10
        return reverse

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseNumber(25))
