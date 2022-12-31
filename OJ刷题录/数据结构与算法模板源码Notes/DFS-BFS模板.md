**二叉树的深度优先遍历(先序遍历)和广度优先遍历(层次遍历)**








## 1.1. 层级遍历


层序遍历的一些变种题目：

-   [LeetCode 103. Binary Tree Zigzag Level Order Traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/) 之字形层序遍历
-   [LeetCode 199. Binary Tree Right Side View](https://leetcode-cn.com/problems/binary-tree-right-side-view/) 找每一层的最右结点
-   [LeetCode 515. Find Largest Value in Each Tree Row](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/) 计算每一层的最大值
-   [LeetCode 637. Average of Levels in Binary Tree](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/) 计算每一层的平均值

对于最短路径问题，还有两道题目也是求网格结构中的最短路径，和我们讲解的距离岛屿的最远距离非常类似：

-   [LeetCode 542. 01 Matrix](https://leetcode-cn.com/problems/01-matrix/)
-   [LeetCode 994. Rotting Oranges](https://leetcode-cn.com/problems/rotting-oranges/)

还有一道在真正的图结构中求最短路径的问题：

-   [LeetCode 310. Minimum Height Trees](https://leetcode-cn.com/problems/minimum-height-trees/)

经过了本文的讲解，相信解决这些题目也不是难事。


https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/

# 2. 深度优先DFS
 



```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        dfs(res, root, 0);
        return res;
    }
    void dfs(vector<vector<int>>& res, TreeNode* root, int level) {
        if (!root) return;
        if (level >= res.size())
            res.push_back(vector<int>());
        res[level].push_back(root->val);
        dfs(res, root->left, level + 1);
        dfs(res, root->right, level + 1);
    }
};

```



作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/




100

101


200





721







# 3. 广度优先搜索BFS
   https://labuladong.github.io/algo/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/BFS%E6%A1%86%E6%9E%B6.html  BFS 解题框架

BFS总共有两个模板：

如果不需要确定当前遍历到了哪一层，BFS模板如下。

```
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过：
            queue.push(该节点)
```
如果要确定当前遍历到了哪一层，BFS模板如下。
这里增加了level表示当前遍历到二叉树中的哪一层了，也可以理解为在一个图中，现在已经走了多少步了。size表示在当前遍历层有多少个元素，也就是队列中的元素数，我们把这些元素一次性遍历完，即把当前层的所有元素都向外走了一步。

```
level = 0
while queue 不空：
    size = queue.size()
    while (size --) {
        cur = queue.pop()
        for 节点 in cur的所有相邻节点：
            if 该节点有效且未被访问过：
                queue.push(该节点)
    }
    level ++;
```



```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> que;
        que.push(root);
        vector<vector<int>> res;
        while (que.size() != 0) {
            int size = que.size();
            vector<int> level;
            while (size --) {
                TreeNode* cur = que.front();
                que.pop();
                if (!cur) {
                    continue;
                }
                level.push_back(cur->val);
                que.push(cur->left);
                que.push(cur->right);
            }
            if (level.size() != 0) {
                res.push_back(level);
            }
        }
        return res;
    }
};


```
上面两个是通用模板，在任何题目中都可以用，是要记住的！

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/


、

```cpp
// 计算从起点 start 到终点 target 的最近距离
int BFS(Node start, Node target) {
    Queue<Node> q; // 核心数据结构
    Set<Node> visited; // 避免走回头路

    q.offer(start); // 将起点加入队列
    visited.add(start);
    int step = 0; // 记录扩散的步数

    while (q not empty) {
        int sz = q.size();
        /* 将当前队列中的所有节点向四周扩散 */
        for (int i = 0; i < sz; i++) {
            Node cur = q.poll();
            /* 划重点：这里判断是否到达终点 */
            if (cur is target)
                return step;
            /* 将 cur 的相邻节点加入队列 */
            for (Node x : cur.adj())
                if (x not in visited) {
                    q.offer(x);
                    visited.add(x);
                }
        }
        /* 划重点：更新步数在这里 */
        step++;
    }
}
```

559



690








200


207














