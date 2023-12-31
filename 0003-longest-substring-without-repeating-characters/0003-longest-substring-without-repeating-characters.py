class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        start = 0
        max_len = 0
        seen = {}

        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = i
            max_len = max(max_len, i - start + 1)
        return max_len
    