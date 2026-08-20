class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPrime(5))
