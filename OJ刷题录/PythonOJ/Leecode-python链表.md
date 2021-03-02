

# python链表

链表(linked_list)是物理存储单元上非连续的、非顺序的存储结构，数据元素的逻辑顺序是通过链表的指针地址实现，每个元素包含两个结点，一个是存储元素的数据域 (内存空间)，另一个是指向下一个结点地址的指针域。根据指针的指向，链表能形成不同的结构，例如单链表，双向链表，循环链表等。


链表通过将链点 i 与其邻居链点 i+1 通过指针相关联，从索引 0 到索引 N-1 对链点进行排序。






链表属于常见的一种线性结构，对于插入和移除而言，时间复杂度都为 O(1)

但是对于搜索操作而言，不管从链表的头部还是尾部，都需要遍历 O(n)，所以最好复杂度为 O(1)，最坏的情况就是从头部遍历到尾部才搜索出对应的元素，所以最坏复杂度为 O(n)，平均复杂度为 O(n)。

归纳如下：

最好复杂度为 O(1)
最坏复杂度为 O(n)
平均复杂度为 O(n)


[LinkedList](file:///D:/tridu33/jupyternotebook/OnlinePythonTutor/v5-unity/src/python/dataStructure/LL/LinkedList.py)



双向链表（Double_linked_list）也叫双链表，是链表的一种，它的每个数据结点中都有两个指针，分别指向直接后继和直接前驱。所以，从双向链表中的任意一个结点开始，都可以很方便地访问它的前驱结点和后继结点。



[DoubleLinkedList](file:///D:/tridu33/jupyternotebook/OnlinePythonTutor/v5-unity/src/python/dataStructure/LL/DLinkedList.py)

双链表










[实python现（列表放着不用用链表）https://blog.csdn.net/qq_43779324/article/details/104968597](https://blog.csdn.net/qq_43779324/article/details/104968597)


Java、Python中没有指针，怎么实现链表、图等数据结构？ - rainoftime的回答 - 知乎 https://www.zhihu.com/question/22680562/answer/36439335




线性数据中的典型顺序表和链表已经讲完：

《[顺序表数据结构在python中的应用](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI2OTQ1NzEyMQ%3D%3D%26mid%3D2247484317%26idx%3D1%26sn%3D07fedcd9a9b21554f988a7a0297fa761%26chksm%3Deae14013dd96c905a5aed9b05a5bcfdc92dee3b44cbba901335642c1700b06afad92c3621c52%26scene%3D21%23wechat_redirect)》

《[python实现单向链表数据结构及其基本方法](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI2OTQ1NzEyMQ%3D%3D%26mid%3D2247484323%26idx%3D1%26sn%3D497036bb2c2e4ec29917319c5004fcad%26chksm%3Deae1402ddd96c93b08ce3c5ec52e2f3c6cc81e6321dd36ce9100105c6677424d7beb97acc402%26scene%3D21%23wechat_redirect)》

《[python实现单向循环链表数据结构及其方法](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI2OTQ1NzEyMQ%3D%3D%26mid%3D2247484329%26idx%3D1%26sn%3D8b6531019b053bf0cc112716c426c7dc%26chksm%3Deae14027dd96c931cfec7afbc917093141acdd246a8635ec9cab66eab0b53d9aee14865095f6%26scene%3D21%23wechat_redirect)》

《[python实现双向链表基本结构及其基本方法](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI2OTQ1NzEyMQ%3D%3D%26mid%3D2247484341%26idx%3D1%26sn%3Df7faf926cd15ccb6e21304066d86a4b2%26chksm%3Deae1403bdd96c92de2b948418eb96f75563498d11905ebaa96ca72d234604c3178a07fa6bd79%26scene%3D21%23wechat_redirect)》

《[python实现双向循环链表基本结构及其基本方法](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI2OTQ1NzEyMQ%3D%3D%26mid%3D2247484347%26idx%3D1%26sn%3D1cefd972158a249046aaa2fc68af1ac0%26chksm%3Deae14035dd96c9234d7739847f0d8df1297fdae2a63db8b6b4e2b84db90fb6c817c619cbe7ba%26scene%3D21%23wechat_redirect)》

《[python实现堆栈数据结构及其基本方法](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI2OTQ1NzEyMQ%3D%3D%26mid%3D2247484353%26idx%3D1%26sn%3Dc949a404d3bef4fcbd8ad3ab5a5d7078%26chksm%3Deae1404fdd96c95924773b2c8bb1f60d44dadda39eabe35a27731f382a764e68d87d8c9deae2%26scene%3D21%23wechat_redirect)》

《[Python实现双端队列数据结构及其基本方法](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI2OTQ1NzEyMQ%3D%3D%26mid%3D2247484359%26idx%3D1%26sn%3Dca67a39aa98a2314f88fe3625826573c%26chksm%3Deae14049dd96c95fb0375aca5d91cb40d8f3da99a6dd395c3aafe149c915dc21a903bb38897b%26scene%3D21%23wechat_redirect)》




























[实python现（列表放着不用用链表）https://blog.csdn.net/qq_43779324/article/details/104968597](https://blog.csdn.net/qq_43779324/article/details/104968597)


Java、Python中没有指针，怎么实现链表、图等数据结构？ - rainoftime的回答 - 知乎 https://www.zhihu.com/question/22680562/answer/36439335






cnblogs.com/NSGUF/p/9157903.html


```python
# 链表节点
class ListNode(object):
    def __init__(self, x):
        self.val = x # 节点值
        self.next = None
```

```python
# 将列表转换成链表
def stringToListNode(input):
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)# 分别将列表中每个数转换成节点
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr
```


```python
# 将链表转换成字符串
def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"
```


```python
class Solution(object):
    # 删除链表中的节点
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        # print(listNodeToString(node))
    # 删除链表的倒数第N个节点
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listNode = []
        while head:# 将每个节点存放在列表中
            listNode.append(head)
            head = head.next
        if 1 <= n <= len(listNode):# 如果n在列表个数之内的话
            n = len(listNode) - n# n原本是倒数位置，现在赋值为正方向位置
            if n == 0:# 如果是删除第1个位置的节点
                if len(listNode) > 1:# 如果节点总数大于1
                    listNode[0].val = listNode[1].val# 删除第1个位置
                    listNode[0].next = listNode[1].next
                else:
                    return None# 因为节点一共就1个或0个，所以删除1个直接返回None
            else:
                listNode[n - 1].next = listNode[n].next# 将该节点的上一个节点的后节点赋值为该节点的后节点，即删除该节点
        return listNode[0]
    # 反转链表
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listNode = []
        while head:
            listNode.append(head)
            head = head.next
        if len(listNode) == 0:
            return None
        for i in range(int(len(listNode) / 2)):# 将节点的值收尾分别调换
            listNode[i].val, listNode[len(listNode) - i - 1].val = listNode[len(listNode) - i - 1].val, listNode[i].val
        return listNode[0]
    # 合并两个有序链表
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newList = ListNode(0)
        newList.next = l1
        prev= newList# 获得新链表

        while l2:
            if not l1:# 如果l1不存在，直接返回l2即可
                prev.next = l2
                break
            if l1.val > l2.val:# 1，判断l1和l2哪个大，如果l2小，则将新节点的后面设为l2的头节点，并将头节点的后面设置为l1，反之l1小，则直接将头节点的后面设置为l1，并将节点后移
                temp = l2
                l2 = l2.next
                prev.next = temp
                temp.next = l1
                prev = prev.next#
            else:# 反之l2大于l1，则是l1节点向后移
                l1, prev = l1.next, l1
        return newList.next
    # 回文链表
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listNode = []
        while head:
            listNode.append(head)
            head = head.next
        for i in range(int(len(listNode) / 2)):# 判断两头的值是否一样大
            if listNode[i].val != listNode[len(listNode) - i - 1].val:
                return False
        return True
    # 环形链表
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1=p2=head
        while p2.next and p2.next.next:# p1走1步，p2走两步，如果在链表没走完的情况下，找到完全相同的节点，就是找到环了
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                return True
        return False

head = [1,2,3,4,5]
head2 = [4, 5, 8, 9]
s = Solution()

# print(s.deleteNode(stringToListNode(head))) 
# print(listNodeToString(s.removeNthFromEnd(stringToListNode(head), 1)))  # 删除倒数第一个位置
# print(listNodeToString(s.reverseList(stringToListNode(head))))  # 翻转
# print(listNodeToString(s.mergeTwoLists(stringToListNode(head2), stringToListNode(head))))  # 合并两个链表
# print(s.isPalindrome(stringToListNode(head)))
# print(s.hasCycle(stringToListNode(head)))
```

```python

```



```python

```



```python

```


```python

```




