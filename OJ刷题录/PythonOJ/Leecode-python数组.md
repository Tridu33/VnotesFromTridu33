
# Leecode-python数组

cnblogs.com/NSGUF/p/9145852.html





```python
# -*- coding: utf-8 -*-
"""
@Created on 2018/6/3 17:06

@author: ZhifengFang
"""


# 排列数组删除重复项
def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    i = 1
    while len(nums) != i:
        if nums[i] == nums[i - 1]:
            del nums[i]
            i -= 1
        i += 1
    return len(nums)


# 买卖股票最佳时机2
def maxProfit(prices):
    max = 0
    if len(prices) <= 1:
        return 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            max += prices[i + 1] - prices[i]
    return max


# 旋转数组
def rotate(nums, k):
    # nums = nums[-k:] + nums[:k + 1]
    # print(nums)
    if len(nums) > 1:
        k = k % len(nums)
        if k != 0:
            temp = nums[-k:]
            nums[k:] = nums[:len(nums) - k]
            nums[0:k] = temp
    print(nums)


# 判断数组中是否有重复元素
def containsDuplicate(nums):
    # if len(nums)>len(set(nums)):
    #     return True
    # return False
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False


# 获得里面只出现一次的数字
def singleNumber(nums):
    numCounts = {}
    result = []
    for num in nums:
        numCounts[num] = numCounts.get(num, 0) + 1
    for key in numCounts.keys():
        if numCounts.get(key) == 1:
            result.append(key)
            break
    return result[0]


# 两个数组的交集 II
def intersect(nums1, nums2):
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1
    newNums = []
    i = 0
    while i < len(nums1):
        j = 0
        while j < len(nums2):
            if nums1[i] == nums2[j]:
                newNums.append(nums2[j])
                del nums1[i], nums2[j]
                i -= 1
                j -= 1
                break
            j += 1
        i += 1
    return newNums


# print(intersect([9],[7,8,3,9,0,0,9,1,5]))


# 加1
def plusOne(digits):
    strDigits = ''
    for example in digits:
        strDigits += str(example)
    strDigits = int(strDigits) + 1
    listDigits = [int(str) for str in str(strDigits)]
    return listDigits


# print(plusOne([1, 2, 3]))


# 移动0
def moveZeroes(nums):
    # for i in range(len(nums)):
    i = 0
    zeroesCount = 0
    while i + zeroesCount < len(nums):
        if nums[i] == 0:
            nums[i:] = nums[i + 1:] + [0]
            i -= 1
            zeroesCount += 1
        i += 1
    return nums


# 两数和
def twoSum(nums, target):
    d = {}
    for x in range(len(nums)):
        a = target - nums[x]
        if nums[x] in d:
            return d[nums[x]], x
        else:
            d[a] = x


nums = [3, 2, 4]
target = 6


# print(twoSum(nums, target))

def isXT(strs):
    strSet = set(strs)
    for s in strSet:
        if s != ".":
            if strs.count(s) > 1:
                return False
    return True


# 有效的数独
def isValidSudoku(board):
    for i in range(9):
        boardLie = [example[i] for example in board]
        key1 = int(i / 3) * 3 + 1
        key2 = 1 + (i % 3) * 3
        boardGe = [board[key1 - 1][key2 - 1], board[key1 - 1][key2], board[key1 - 1][key2 + 1],
                   board[key1][key2 - 1], board[key1][key2], board[key1][key2 + 1],
                   board[key1 + 1][key2 - 1], board[key1 + 1][key2], board[key1 + 1][key2 + 1]]
        if isXT(board[i]) == False:
            return False
        if isXT(boardLie) == False:
            return False
        if isXT(boardGe) == False:
            return False
    return True


board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
         [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]


# print(isValidSudoku(board))
# 旋转图像
def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
    print(matrix)

ma = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(ma)
```






































