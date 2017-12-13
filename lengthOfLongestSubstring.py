class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        start = 0
        while start < len(s):
            li = list()
            for c in s[start:]:
                if c in li:
                    break
                else:
                    li.append(c)
            result = max(result, len(li))
            start = start + 1

        return result


so = Solution()
print so.lengthOfLongestSubstring('abccsdvbcnmc')
