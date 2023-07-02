class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        result = 0
    
        while x:
            x, last_digit = divmod(x, 10)
            result = result * 10 + last_digit
    
            if result < -2**31 or result > 2**31 - 1:
                return 0
    
        return -result if is_negative else result
        