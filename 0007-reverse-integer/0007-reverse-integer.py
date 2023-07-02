class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        is_negative = x < 0
        x = abs(x)
        result = 0
    
        while x:
            digit = x % 10
            x //= 10
    
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
                return 0
            if result < MIN_INT // 10 or (result == MIN_INT // 10 and digit < -8):
                return 0
    
            result = result * 10 + digit
    
        return -result if is_negative else result
        