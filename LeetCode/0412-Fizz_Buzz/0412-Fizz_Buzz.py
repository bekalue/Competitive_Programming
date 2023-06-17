"""A module that contains an answer for fizzbuzz problem on leetcode."""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_arr = []
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                str_arr.append("FizzBuzz")
            elif (i % 3 == 0) and (i % 5 != 0):
                str_arr.append("Fizz")
            elif (i % 3 != 0) and (i % 5 == 0):
                str_arr.append("Buzz")
            else:
                str_arr.append(str(i))
        return str_arr