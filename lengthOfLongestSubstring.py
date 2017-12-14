# coding=utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        start = 0
        while start < len(s):
            li = ''  # 如果用list会超时  说明字符串拼接效率更高
            tmp = len(s)
            for c in s[start:]:
                if c in li:
                    tmp = li.index(c) + 1
                    break
                else:
                    li += c
            result = max(result, len(li))
            start += tmp
        return result

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = []

        if len(s) == 1:
            return 1
        i = 0
        j = 1
        while i <= len(s) - 1:
            while j <= len(s):
                if s[j] not in s[i:j]:
                    if j == len(s) - 1:
                        if len(substr) < len(s[i:j +1]):
                            substr = s[i:j + 1]
                        return len(substr)
                    j += 1
                else:
                    if len(s[i:j]) > len(substr):
                        substr = s[i:j]
                    i += 1
        return len(substr)

so = Solution()
print so.lengthOfLongestSubstring('abccsdvbcnmc')
print so.lengthOfLongestSubstring2('abccsdvbcnmc')
