class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        number = int(''.join(s))
        number += 1
        return [int(x) for x in str(number)]
        