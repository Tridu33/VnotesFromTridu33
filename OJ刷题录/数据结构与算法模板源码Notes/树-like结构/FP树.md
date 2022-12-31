# 1. FP树
https://www.cnblogs.com/pinard/p/6307064.html

作为一个挖掘频繁项集的算法，
Apriori算法需要多次扫描数据，I/O是很大的瓶颈。为了解决这个问题，FP Tree算法（也称FP Growth算法）采用了一些技巧，无论多少数据，只需要扫描两次数据集，因此提高了算法运行的效率。下面我们就对FP Tree算法做一个总结。





FPtree树 https://blog.csdn.net/qq_37671037/article/details/98590039


```python
本代码使用节点类TreeNode与树类MultiTree实现了FPtree树的构建
本代码使用networkx库函数显示化绘制FPtree树结构，得到的是条件模式积所对应的树
得到的树结构节点上的信息，如b0:2, b为项的字母，字母后的数字'0'是为了与其他分支上的b节点名不重复，数字的具体含义为节点第
一次插入到树是原始数据的第几条；数字'2'指本节点的支持度为2
得到条件模式积所对应的树后，将首字母相同的节点(如b0与b1)对应的支持度相加，得到本项在本树中所对应的支持度，选择所有支持度
和大于等于最小支持度的项为频繁项集
得到的根节点名如 atree:1, 'a'表示a条件下所对应的FPtree；其对应的数字'1'为方便绘制，本身无意义
实验结果截图在  \结果截图\实验2-FPTree给出
import operator
import networkx as nx
import matplotlib.pyplot as plt
# 存储所有条件FPtree树
Tree = []
# 储存每个FPtree条件树每个元素支持度
Treedir = {}
# 原始数据
database = [['a','b','c','d','e','f','g','h'],
            ['a','f','g'],
            ['b','d','e','f','j'],
            ['a','b','d','i','k'],
            ['a','b','e','g']]
# 最小支持度，在Inputdata函数中赋值
supmin = 3
def Inputdata():
    # 得到符合最小支持度数据库数据
    num = 5
    # 记录频繁项集
    data = {}
    dir = []
    for j in range(num):
        dir = [r for ro in database for r in ro]
    for x in dir:
        if x in data:
            data[x] += 1
        else:
            data[x] = 1
    keys = list(data.keys())
    for x in keys:
        if data[x] < supmin:
            data.pop(x)
    sorted(data.items(),key=operator.itemgetter(1),reverse=True)
    return data
# 得到每一项去掉小于最小支持度的元素并排序后的集

class TreeNode(object):
    '''
    树的节点类
    '''
    def __init__(self, name):
        self.name = name
        self.children = []
        self.num = 1

class MultiTree(object):
    '''
    树的类
    实现增、删、改、查
    '''

    def __init__(self, tree_root_name='root'):
        self.count = 0
        self.tree = TreeNode(tree_root_name)
        self.nlist = []
        self.Alist = []

    def add(self, nodelist, i):
        if not nodelist:
            return 1
        node = TreeNode(nodelist[0] + str(i))
        x = 0
        self.if_node_exist_recursion(self.tree,nodelist,x,i)
        n = self.nlist[0]
        A = self.Alist[0]
        self.Alist = []
        self.nlist = []
        for j in range(n,len(nodelist)):
            node = TreeNode(nodelist[j] + str(i))
            if j==n:
                self.add_recursion(A, node,self.tree)

            else:
                parentname = nodelist[j-1] + str(i)
                self.add_recursion(parentname,node,self.tree)

    def show_tree(self):
        '''
        利用networkx转换成图结构，方便结合matplotlib将树画出来
        '''
        G = nx.Graph()
        self.to_graph_recursion(self.tree, G)
        nx.draw(G, with_labels=True)
        plt.show()

    def to_graph_recursion(self, tree, G):
        '''
        将节点加入到图中
        '''
        G.add_node(tree.name+ ": "+str(tree.num))
        for child in tree.children:
            G.add_nodes_from([tree.name+ ": "+str(tree.num), child.name+ ": "+str(child.num) ])
            G.add_edge(tree.name+ ": "+str(tree.num), child.name+ ": "+str(child.num))
            self.to_graph_recursion(child, G)

    def if_node_exist_recursion(self, tree, nodelist, x, i):
        '''
        tree:需要判断是否存在node节点的树
        nodelist:需要添加的节点的列表
        x:记录本次迭代需要对列表的第几个项进行操作
        i:记录本的迭代中对二维列表中第几列进行操作
        '''
        node = TreeNode(nodelist[x]+str(i))
        name = list(node.name)[0]
        nodex = tree.name
        for child in tree.children:
            if list(child.name)[0] == name:
                child.num +=1
                if x == len(nodelist)-1:
                    self.Alist.append(child.name)
                    self.nlist.append(x+1)
                    break
                else:
                    x = x+1
                    self.if_node_exist_recursion(child,nodelist,x,i)
                    self.Alist.append(child.name)
                    self.nlist.append(x)
        # x为列表中的第几个项需要下个函数添加到树中
        # nodex为需要添加到父类节点的名字
        self.Alist.append(tree.name)
        self.nlist.append(x)
        return 1

    def add_recursion(self, parent, node, tree):
        '''
        增加节点时使用的递归函数
        '''
        if parent == tree.name:
            tree.children.append(node)
            return 1
        for child in tree.children:
            if child.name == parent:
                children_list = child.children
                children_list.append(node)
                child.children = children_list
                break
            else:
                self.add_recursion(parent, node, child)

def Ordereddata():
    data = Inputdata()
    keys = list(data.keys())
    orderdata1 = []
    for i in range(5):
        orderdata2 = []
        for x in keys:
            if x in database[i]:
                orderdata2.append(x)
        orderdata1.append(orderdata2)

    return orderdata1

def meanwhile():
    # 存储输入数据符合最小支持度后形成的列表 二维列表
    orderdata = Ordereddata()
    keys = list(Inputdata().keys())
    for x in keys.__reversed__():
        # 存储条件约束下需要加入条件树的节点列表
        new_orderdata = []
        # 存储去掉条件后剩余元素 一维列表 如g条件下 存储[a, b, d, e, f]
        li = []
        for y in keys:
            if y!=x:
                # 得到新的x条件下的项集合
                li.append(y)
            else:
                break
        # 查询之前输入的数据集合，去掉不在新的x添加下得到项集合中的元素
        for z in orderdata:
            lli = []
            for s in li :
                if s in z and x in z:
                    lli.append(s)
            # 将本次循环处理后的行输入新数据列中
            new_orderdata.append(lli)
        buildtree_view(x+'tree',new_orderdata)

def buildtree_view(name,orderdata):
    '''
    :param name: 条件FPtree名
    :param orderdata: 本次条件下输入的集
    建树与添加节点并显示话
    '''
    T = MultiTree(name)
    i = 0
    for x in orderdata:
        T.add(x, i)
        i += 1
    Tree.append(T)
    T.show_tree()

def tree_result(Tree):
    data = Inputdata()
    keys = list(data.keys())
    global Treedir
    for T in Tree:
        pr = []
        for x in keys:
            Treedir[x] = 0
        tree_result_recursion(T.tree)
        for y in Treedir:
            if Treedir[y] >= supmin:
                pr.append(y)
        if len(pr)!=0:
            pr.append(list(T.tree.name)[0])
            print(list(T.tree.name)[0] + "条件下FPtree频繁项集为：" + str(pr))
        else:
            print(list(T.tree.name)[0] + "条件下FPtree频繁项集为：" + str(pr))

def tree_result_recursion(T):
    global Treedir
    listt = list(T.name)
    Treedir[listt[0]] +=T.num
    for child in T.children:
        tree_result_recursion(child)

def main():
    meanwhile()
    tree_result(Tree)
if __name__ == '__main__':
    main()
   

```


























