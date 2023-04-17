
"""

求子集算法-循环、递归、回溯、位运算 - 翩翩少年的文章 - 知乎
https://zhuanlan.zhihu.com/p/347663905
"""


# loop
def loop_subset(arr):
    res_all = [[]]
    for i in arr:
        res_all.extend([re+[i] for re in res_all])
    return res_all

print('loop_subset:\n')
nums = [1,2,3]
res_loop = loop_subset(nums)
print(res_loop)
# rec
rec_result_all = [[]]
def recursion_subset(arr,n):
    if n==1:
        rec_result_all.append([1])
        return rec_result_all
    else:
        rec_result_all.extend([a + [arr[n-1]] for a in recursion_subset(arr, n-1)])
    return rec_result_all

print('recursion_subset:\n')
n=len(nums)
recursion_subset(nums,len(nums))
print(rec_result_all)



# 
nums = [1,2,3]
def backtracking_subset(nums):
    def backtrack(first=0, curr=[]):
        ## 递归函数的出口
        if len(curr) == k:
            res.append(curr[:])
        ## 设计递归函数结构
        for i in range(first, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    res = []
    for k in range(len(nums) + 1):
        # 计算每一类的子集
        backtrack()
    return res


print('backtracking_subset:\n')
nums = [1,2,3]
res_loop = backtracking_subset(nums)
print(res_loop)

# yield_subset https://stackoverflow.com/questions/8711596/python-3-s-for-s-in-subsetss-and-yield
def subsets(aList):

       if aList ==[]:   # base case
          yield []
       else:
          first = aList[0]
          rest  = aList[1:]
          for ss in subsets(rest):  # include first or don't in each
              yield ss                   # subset of rest
              yield [first]+ss

print ("\n testing subsets")
S = ['A','B','C','D','E']
ss = [s for s in subsets(S)]
print ("The subsets of",S,"are:")
print (ss)




# bit_yield
def PowerSetsBinary_subset(items):
    N = len(items)
    # generate all combination of N items
    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):  # jth bit of Integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

res_bit = PowerSetsBinary_subset(nums)
print(res_bit)

















# ==================================== T9 input method with those different forms:




























