class Solution(object):

    def mergeTwoArrays(self, num1, num2):
        i = 0
        j = 0
        l1 = len(num1)
        l2 = len(num2)

        if l1 == 0:
            return num2
        if l2 == 0:
            return num1

        res = []
        while i < l1 and j < l2 :
            if num1[i] < num2[j]:
                res.append(num1[i])
                i += 1
            elif num1[i] == num2[j]:
                res.append(num1[i])
                res.append(num2[j])
                i+=1
                j+=1
            else:
                res.append(num2[j])
                j+=1

        if i == l1:
            res += num2[j:]
        else:
            res += num1[i:]

        return res


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        num = self.mergeTwoArrays(nums1, nums2)
        print num
        l = len(num)
        while j < l:
            i += 1
            j += 2
        if j == l:
            return float(num[i] + num[i-1])/2
        else:
            return float(num[i-1])


a = [1,2,4,6,8]
b = [2,5,7,11]

s = Solution()
print s.findMedianSortedArrays(a, b)
