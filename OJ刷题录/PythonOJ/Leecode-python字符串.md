# Leecode-python字符串





```python
# 反转字符串
def reverseString(s):
    return s[::-1]


# 颠倒数字
def reverse(x):
    if x < 0:
        flag = -2 ** 31
        result = -1 * int(str(x)[1:][::-1])
        if result < flag:
            return 0
        else:
            return result
    else:
        flag = 2 ** 31 - 1
        result = int(str(x)[::-1])
        if result > flag:
            return 0
        else:
            return result


# 字符串中的第一个唯一字符
def firstUniqChar(s):
    d = {}
    for i in range(len(s)):
        d[s[i]] = d.get(s[i], 0) + 1
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1


# 有效的字母异位词
def isAnagram(s, t):
    if len(t) != len(s):
        return False
    if len(set(t)) != len(set(s)):
        return False
    for ex in set(t):
        if s.count(ex) != t.count(ex):
            return False
    return True


# 验证回文字符串
def isPalindrome(s):
    import re
    s = s.lower()
    newS = re.sub(r'[^A-Za-z0-9]', "", s)
    if newS[::-1] == newS:
        return True
    else:
        return False


# 字符串转整数（atoi）
def myAtoi(str):
    import re
    if re.match('\s+', str) != None:
        a, b = re.match('\s+', str).span()
        str = str[b:]
    if str == '':
        return 0
    flag = True
    if str[0] == '-':
        str = str[1:]
        flag = False
    elif str[0] == '+':
        str = str[1:]
    if re.match('\d+', str) != None:
        a, b = re.match('\d+', str).span()
        str = str[a:b]
        if flag == True:
            if int(str) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return int(str)
        else:
            if -1 * int(str) < -2 ** 31:
                return -2 ** 31
            return -1 * int(str)
    else:
        return 0


# 实现 strStr() 函数。
def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


# 数数并说
def countAndSay(n):
    keyStr = '1'  # 从1开始
    for i in range(n - 1):  # 循环n次
        newStr = ""  # 存储新的字符
        strList = []  # 循环一个字符串下来获取每个字符的个数
        sList = []  # 相同字符的个数
        flag = True
        for j in range(len(keyStr) - 1):  # 循环字符的长度减一 flag表示默认最后一个字符和前面一个字符不同，
            sList.append(keyStr[j])
            sList.append(1)
            if keyStr[j] == keyStr[j + 1]:  # 如果当前位置的字符和下一个位置的字符相同
                sList[1] += 1
                flag = False
            else:
                strList.append(sList)  # 不同的话 将上一个字符的情况存储进列表
                sList = []
                flag = True
        if flag:  # 如果最后一个字符和前一个字符不同，则将字符情况加入
            strList.append([keyStr[-1], 1])
        else:
            if sList != []:  # 最后一串相同字符加入列表
                strList.append(sList)
        for k in range(len(strList)):  # 将列表的字符按顺序取出
            newStr = newStr + '' + str(strList[k][1])
            newStr = newStr + '' + strList[k][0]
        keyStr = newStr
    return keyStr


# 最长公共前缀
def longestCommonPrefix(strs):
    if strs == []:
        return ''
    lenKey = len(strs[0])
    key = 0
    longest = 0
    for i in range(1, len(strs)):
        if len(strs[i]) < lenKey:
            key = i
            lenKey = len(strs[i])
    for i in range(len(strs[key])):
        flag = True
        for j in range(len(strs)):
            if strs[j][i] != strs[key][i]:
                flag = False
        if flag:
            longest += 1
        else:
            break
    return strs[key][0:longest]
```





