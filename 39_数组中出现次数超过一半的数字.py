# 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
#       由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# 思路一：排序数组，比较中间数的个数是否大于数组长度的一半，时间复杂度为O(nlogn)


class Solution(object):
    def MoreThanHalfNum_Solution(self, numbers):
        numbers.sort()

        tmp = numbers[len(numbers)//2]

        if numbers.count(tmp) > len(numbers)/2:
            return tmp
        else:
            return 0

# 思路二:根据数组特点。时间复杂度O(n)，空间复杂度O(1)
#        对数组进行遍历：如果遍历到下一个数字的时候，下一个数字与当前数字相同，次数加1，
#        与当前数字不同，次数减1，
#        如果次数为0，则要保存下一个数字，并把次数设置为1


class Solution1(object):
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        res = 0
        times = 0
        for i in range(len(numbers)):
            if times == 0:
                res = numbers[i]
                times = 1
            elif numbers[i] == res:
                times += 1
            else:
                times -= 1
        if numbers.count(res) > len(numbers) / 2:
            return res
        else:
            return 0


# 第三种思路：基于patition的时间复杂度为O(n)
class Solution2(object):
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        left = 0
        right = len(numbers) - 1

        middle = len(numbers) >> 1

        index = self.Partition(numbers, left, right)

        while index != middle:
            if index > middle:
                right = index - 1
                index = self.Partition(numbers, left, right)
            else:
                left = index + 1
                index = self.Partition(numbers, left, right)

        result = numbers[middle]

        if not self.CheckMoreThanHale(numbers, result):
            return 0
        return result

    def Partition(self, numbers, left, right):
        pivot = numbers[left]

        while left < right:
            while left < right and numbers[right] >= pivot:
                right -= 1
            while left < right and numbers[left] <= pivot:
                left += 1
            numbers[left], numbers[right] = numbers[right], numbers[left]

        return left

    def CheckMoreThanHale(self, numbers, result):
        count = 0

        for i in range(len(numbers)):
            if numbers[i] == result:
                count += 1
        if count <= len(numbers) / 2:
            return False
        else:
            return True


# 第四种思路：使用python标准库collections，Counter是一个简单的计数器
#             most_common([n])函数，返回一个TopN列表。
#             如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的。
# 教程：http://www.pythoner.com/205.html
class Solution3(object):
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        from collections import Counter
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers) / 2:
            return count[0][0]
        return 0


# 哈希表的思想，时间复杂度O(n)，空间复杂度O(n)
class Solution4(object):
    def MoreThanHalfNum_Solution(self, numbers):
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] not in dic:
                dic[numbers[i]] = 1
            else:
                dic[numbers[i]] += 1
        for key in dic:
            if dic[key] > len(numbers) / 2:
                return key
        return 0


S = Solution1()
print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum_Solution([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum_Solution([1, 2]))
