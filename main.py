class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        # will be zero if and only if n is a power of two, as only one bit will be set in n
        return n & (n-1) == 0

        # while n > 1:
        #     if n%2 != 0: # Odd number
        #         return False
        #     else:
        #         n = n//2
        # return True   
