




python中的树数据结构 - python之战的文章 - 知乎
https://zhuanlan.zhihu.com/p/62005586


[Python -二叉树 创建与遍历算法(很详细）](https://www.cnblogs.com/sxf1061700625/p/11319617.html)


Python treelib库创建多叉树的用法介绍

blog.csdn.net/weixin_43790276/article/details/108248298?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.channel_param





下面将说图形结构中的典型数据机构：树；是一种重要的非线性数据结构，直观地看，它是数据元素（在树中称为结点）按分支关系组织起来的结构，很象自然界中的树那样。



**常用树的分类：**

**无序树**树中任意节点的子节点之间没有顺序关系，这种树称为无序树，也称为自由树；

**有序树**树中任意节点的子节点之间有顺序关系，这种树称为有序树；

**二叉树**每个节点最多含有两个子树的树称为二叉树；

**完全二叉树**对于一颗二叉树，假设其深度为d(d>1)。除了第d层外，其它各层的节点数目均已达最大值，且第d层所有节点从左向右连续地紧密排列，这样的二叉树被称为完全二叉树，其中满二叉树的定义是所有叶节点都在最底层的完全二叉树;



--------------------------------------------------------------------


**排序二叉树**（二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树）左小右大；




它主要用于搜索。 它或者是一棵空树，或者是具有下列性质的二叉树：

若左子树不空，则左子树上所有结点的值均小于它的根结点的值；

若右子树不空，则右子树上所有结点的值均大于它的根结点的值；

左、右子树也分别为二叉排序树






**平衡二叉树（AVL树**：当且仅当任何节点的两棵子树的高度差不大于1的二叉树；


平衡二叉树(平衡二叉树又被称为 AVL 树 )是基于二分法的策略提高数据的查找速度的二叉树的数据结构。

特点：平衡二叉树是采用二分法思维把数据按规则组装成一个树形结构的数据，用这个树形结构的数据减少无关数据的检索，大大的提升了数据检索的速度；平衡二叉树的数据结构组装过程有以下规则：

非叶子节点只能允许最多两个子节点存在。

每一个非叶子节点数据分布规则为左边的子节点小于前节点的值，右边的子节点大于当前节点的值(这里值是基于自己的算法规则而定的，比如 hash 值)。


**霍夫曼树**（用于信息编码）：带权路径最短的二叉树称为哈夫曼树或最优二叉树；







**B B- B+树**：一种对读写操作进行优化的自平衡的二叉查找树，能够保持数据有序，拥有多余两个子树。

------------------------------------------------------------------------------------




cnblogs.com/NSGUF/p/9221811.html LeetCode 二叉树实现



```python
# 定义二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 

```



遍历原理：

二叉树的遍历：是指从根结点出发，按照某种次序依次访问二叉树中的所有结点，使得每个结点被访问一次且仅被访问一次。

这里有两个关键词：访问和次序。

访问其实是要根据实际的需要来确定具体做什么，比如对每个结点进行相关计算，输出打印等。它算作是一个抽象操作。

二叉树的遍历次序不同于线性结构，最多也就是从头到尾、循环和双向等简单的遍历方式。树的结点之间不存在唯一的前驱和后继关系，在访问一个结点后，下一个被访问的结点面临着不同的选择。






前序遍历（**根**左右）
前序遍历首先访问根节点，然后遍历左子树，最后遍历右子树。

中序遍历（左**根**右）
中序遍历是先遍历左子树，然后访问根节点，然后遍历右子树。

后续遍历（左右**根**）
后序遍历是先遍历左子树，然后遍历右子树，最后访问树的根节点。

层次遍历
该算法从一个根节点开始，首先访问节点本身。 然后遍历它的相邻节点，其次遍历它的二级邻节点、三级邻节点，以此类推。

```python
class Solution:
    # 前序遍历
    def solvePre(self, root, result):
        if root == None:
            return []
        result.append(int(root.val))  # 先添加根节点
        self.solvePre(root.left, result)  # 再添加左子树
        self.solvePre(root.right, result)  # 再添加又子树
        return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.solvePre(root, [])

    # 中序遍历
    def solveIno(self, root, result):
        if root == None:
            return []
        self.solveIno(root.left, result)  # 先遍历左子树
        result.append(int(root.val))
        self.solveIno(root.right, result)  # 再遍历右子树
        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.solveIno(root, [])

    # 后序遍历
    def solvePos(self, root, result):
        if root == None:
            return []
        self.solvePos(root.left, result)  # 先访问左子树
        self.solvePos(root.right, result)  # 在访问右子树
        result.append(int(root.val))
        return result

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.solvePos(root, [])

    # 层次遍历
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]  # 通过list存储
        result = []
        index = 0
        while True:
            start = index  # 该层的节点在list中的开始位置
            end = len(queue)  # 该层的节点在list中的最后位置
            block = []  # 存储该层的数据
            for i in range(start, end):
                block.append(queue[i].val)
                if queue[i].left != None:
                    queue.append(queue[i].left)
                if queue[i].right != None:
                    queue.append(queue[i].right)
                index += 1
            if start >= end:  # 如果list中的元素被循环完了，即没有添加新的节点
                break
            result.append(block)
        return result

    # 最大深度
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        leftCount = 1  # 左子树的深度
        rightCount = 1  # 右子树的深度
        leftCount = leftCount + self.maxDepth(root.left)
        rightCount = rightCount + self.maxDepth(root.right)
        return max(leftCount, rightCount)  # 选深度大的

    # 对称二叉树
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        index = 0
        queue = [root]
        while True:  # 获取每层的数据存入list，如果list翻转后和list不一样 则表示不是对称的
            start = index
            end = len(queue)
            block = []
            for i in range(start, end):
                if queue[i] == None:
                    block.append(' ')  # 这是为了确定某个地方为空的，里面的数据只有不为数字就行
                else:
                    block.append(queue[i].val)
                    queue.append(queue[i].left)
                    queue.append(queue[i].right)
                index += 1

            if block[::-1] != block:
                return False
            if index >= len(queue):
                break
            if block.count(' ') == len(block):  # 当该层的数据都是空的，则跳出
                break
        return True

    def solveHasPathSum(self, root, sumAll, sum, flag):  # 使用深度搜索
        if root:
            sumAll += root.val
            if root.left or root.right:  # 当该节点不是叶子节点时
                flag = self.solveHasPathSum(root.left, sumAll, sum, flag) | self.solveHasPathSum(root.right, sumAll,
                                                                                                 sum, flag)
            else:
                if sumAll == sum:
                    return True
        return flag

    # 路径总和
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.solveHasPathSum(root, 0, sum, False)

    # 100. 相同的树
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p != None and q != None and p.val == q.val:  # 如果pq相同，则判断他们的子节点是否也相同
            return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        return False

    # 从前序与中序遍历序列构造二叉树
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        root = TreeNode(preorder[0])  # 前序遍历的第一个节点是父节点
        index = inorder.index(preorder[0])  # 父节点的左边是左子树的，右边是右子树的
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

    # 从中序与后序遍历序列构造二叉树
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if postorder == []:
            return None
        root = TreeNode(postorder[-1])  # 后序遍历的最后一个节点是父节点
        index = inorder.index(postorder[-1])  # 父节点的左边是左子树的，右边是右子树的
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root

    # 每个节点的右向指针 II
    def connect(self, root):
        if root != None:
            index = 0
            queue = [root]
            while True:
                start = index
                end = len(queue)
                for i in range(start, end):
                    if i != end - 1:  # 如果该层的最后一个节点，则指向空，否则指向后一个节点
                        queue[i].next = queue[i + 1]
                    else:
                        queue[i].next = None
                    if queue[i].left:  # 节点存在则添加，否则不添加
                        queue.append(queue[i].left)
                    if queue[i].right:
                        queue.append(queue[i].right)
                    index += 1
                if index >= len(queue):
                    break

    def isContent(self, root, num):  # 判断该树是否有该节点
        if root == None:
            return False
        if root.val == num.val:
            return True
        return self.isContent(root.left, num) | self.isContent(root.right, num)

    # 二叉树的最近公共祖先
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root.val == p.val or root.val == q.val:  # 如果根节点是p或q则该节点是lca
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left != None else right

    # 序列化
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []
        queue = [root]
        result = []
        index = 0
        nullIndex = 0
        while True:
            start = index
            end = len(queue)
            flag = True
            for i in range(start, end):
                if queue[i] != None:
                    flag = False
                    continue
            if flag == False:
                for i in range(start, end):
                    if queue[i] == None:
                        result.append('null')
                    else:
                        result.append(queue[i].val)
                        nullIndex = i
                        if queue[i].left != None:
                            queue.append(queue[i].left)
                        else:
                            queue.append(None)
                        if queue[i].right != None:
                            queue.append(queue[i].right)
                        else:
                            queue.append(None)
                    index += 1
            else:
                break

        return result[:nullIndex + 1]

    # 反序列化
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        inputValues = data
        if data == []:
            return None
        root = TreeNode((inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root
```
























# 多叉树

Python的treelib构建多叉树具体的参考 Useful APIs https://treelib.readthedocs.io/en/latest/pyapi.html



```
from treelib import Node, Tree

tree = Tree()

tree.show()

# # 取得根节点到每一个叶节点的标识路径，返回值为标识list列表的list列表（二重列表），根节点不省略

tree.paths_to_leaves()

# # 建议使用remove_node来删除节点，因为remove_subtree将消耗内存以存储新树（返回值）

# # 移除以nid标识的节点，同时移除其所有的子节点 ,返回值为移除的节点个

tree.remove_node( identifier)

# # 移除以nid标识为根节点的一棵子树 ,返回值为移除该子树的树，nid不存在则返回一个空树

remove_subtree(self, nid)

# # 返回所有叶节点对象list列表，若给定root则返回以root为根节点的树的所有叶节点对象list列表

leaves(self, root=None)

# # 返回以nid为标识(identifier)子节点，nid不存在则返回list为空

children(self, nid)

# # 返回以nid为标识(identifier)父节点，nid不存在则返回list为空

parent(self, nid) 


tree.create_node('ROOT','root')  # root node

tree.create_node(temps[yy][xx],temps_id[yy][xx],parent="root")
 
```




Python的treelib构建多叉树——快速命名节点id
blog.csdn.net/u012111465/article/details/82908552

Python的treelib构建多叉树——根据id快速建树
blog.csdn.net/u012111465/article/details/82908601 














