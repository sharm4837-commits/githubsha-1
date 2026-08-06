class Solution:
    def isArmstrong(self, n):
        original = n
        num_digits = len(str(n))
        total = 0
        
        while n > 0:
            last_digit = n % 10
            total += last_digit ** num_digits
            n = n // 10
        
        return original == total

if __name__ == "__main__":
    sol = Solution()
    print(sol.isArmstrong(153))
