# 1. trie树
可以支持数字或字母的字典树模板

```
public class Trie {

    class TrieNode {
        /**
         * 当前节点包含的字符
         */
        char c;

        /**
         * 当前节点字节点集合
         * c -> TrieNode(c)
         * */
        HashMap<Character, TrieNode> children = new HashMap();

        /**
         * 当前节点是否是某个单词的结尾
         * */
        boolean isEnd = false;

        public TrieNode(char c) {
            this.c = c;
        }
    }

    TrieNode root;

    /**
     * Initialize your data structure here.
     */
    public Trie() {
        this.root = new TrieNode('0');
    }

    /**
     * Inserts a word into the trie.
     */
    public void insert(String word) {
        if (word == null || word.isEmpty()) {
            return;
        }
        TrieNode current = root;
        for (char c : word.toCharArray()) {
            current.children.putIfAbsent(c, new TrieNode(c));
            current = current.children.get(c);
        }
        current.isEnd = true;
    }

    /**
     * Returns if the word is in the trie.
     */
    public boolean search(String word) {
        TrieNode last = findLast(word);
        return last != null && last.isEnd;
    }

    /**
     * Returns if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
        return findLast(prefix) != null;
    }

    private TrieNode findLast(String word) {
        if (word == null || word.isEmpty()) {
            return null;
        }
        char[] chars = word.toCharArray();
        int index = 0;
        TrieNode current = root;
        while (index < chars.length) {
            char c = chars[index];
            if (current == null) {
                return null;
            }
            TrieNode child = current.children.get(c);
            if (child == null) {
                return null;
            }
            current = child;
            if (index == chars.length - 1) {
                return child;
            }
            index++;
        }
        return null;
    }
}

```




作者：stay-hungry-2
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/javazi-dian-shu-mo-ban-bu-jin-jin-zhi-chi-zi-mu-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

















字典树实现模板



```
class Trie {
public:
    struct Node{
        bool is_end;
        Node *son[26];
        Node(){
            is_end = false;
            for(int i = 0; i < 26; i++) son[i] = NULL;
        } 
    }*root;
    /** Initialize your data structure here. */
    Trie() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        auto p = root;
        for(auto c : word){
            int u = c - 'a';
            if(p->son[u] == NULL){
                p->son[u] = new Node();
            }
            p = p->son[u];
        }
        p->is_end = true;
    }

    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto p = root;
        for(auto c : word){
            int u = c - 'a';
            if(p->son[u] == NULL) return false;
            p = p->son[u];
        }
        return p->is_end;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto p = root;
        for(auto c : prefix){
            int u = c - 'a';
            if(p->son[u] == NULL) return false;
            p = p->son[u];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

```

作者：Cuiwanxin1998
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/zi-dian-shu-shi-xian-mo-ban-by-cuiwanxin1998/




Trie树的模板题，可以用链表或者数组两种方式来试下Trie的数据结构
Trie树一般用来存储或者索引字符串的集合




数组模拟：



```
const int N = 100010;
class Trie {
        int son[N][26];
        int cnt[N];
        int idx = 0;
        public:
        /** Initialize your data structure here. */
        Trie() {
            memset(son, 0, N * 26 * sizeof(int));
            memset(cnt, 0, N * sizeof(int));
            idx = 0;
        }

        /** Inserts a word into the trie. */
        void insert(string word) {
            int n = word.size();
            int p = 0;
            for (int i = 0; i < n; ++i) {
                int u = word[i] - 'a';
                if (0 == son[p][u]) {
                    son[p][u] = ++idx;
                }
                p = son[p][u];
            }
            cnt[p]++;
        }

        /** Returns if the word is in the trie. */
        bool search(string word) {
            int p = 0;
            for (int i = 0; i < word.size(); ++i) {
                int u = word[i] - 'a';
                if (!son[p][u]) {
                    return false;
                }
                p = son[p][u];
            }
            if (!cnt[p]) return false;
            return true;
        }

        /** Returns if there is any word in the trie that starts with the given prefix. */
        bool startsWith(string prefix) {
            int p = 0;
            for (int i = 0; i < prefix.size(); ++i) {
                int u = prefix[i] - 'a';
                if (!son[p][u]) return false;
                p = son[p][u];
            }
            return true;
        }
};


```


作者：EllieFeng
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/trieshu-mo-ban-shu-zu-mo-ni-shi-xian-c-by-s7ven/


```
struct TrieNode {
    bool isWord;
    TrieNode* children[26];
    TrieNode() : isWord(false) {
        for (auto& child : children) {
            child = nullptr;
        }
    }
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        auto p = root;
        for (const auto& ch : word) {
            int i = ch - 'a';
            if (!p->children[i]) {
                p->children[i] = new TrieNode();
            }
            p = p->children[i];
        }

        p->isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto p = root;
        for (const auto& ch : word) {
            int i = ch - 'a';
            if (!p->children[i]) {
                return false;
            } else {
                p = p->children[i];
            }
        }

        return p->isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto p = root;
        for (const auto& ch : prefix) {
            int i = ch - 'a';
            if (!p->children[i]) {
                return false;
            } else {
                p = p->children[i];
            }
        }

        return true;

    }

private:
    TrieNode* root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

```




作者：jyj407
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/zhong-gui-zhong-ju-trie-mo-ban-ti-mu-by-jyj407/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。








```
/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.root = {}
    this.endWord = "#"
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root
    for (let ch of word ) {
        node[ch] = node[ch] || {}
        node = node[ch]
    }
    node[this.endWord] = this.endWord
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root
    for ( let ch of word ) {
        if(!node[ch]) return false
        node = node[ch]
    }
    return node[this.endWord] === this.endWord 
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root
    for ( let ch of prefix ) {
        if(!node[ch]) return false
        node = node[ch]
    }
    return true
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */

```



作者：FYkapBYcHC
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/triede-mo-ban-by-fykapbychc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。























































