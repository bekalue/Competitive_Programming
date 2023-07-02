class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        modified_str = haystack.replace(needle, 'X')
        if modified_str is haystack:
            return -1
        else:
            return modified_str.index('X')
        