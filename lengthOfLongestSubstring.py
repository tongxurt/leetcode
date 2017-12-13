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
            print start
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


so = Solution()
print so.lengthOfLongestSubstring('abccsdvbcnmc')
