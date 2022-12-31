


# 1. LeeCode-python图




https://www.yiibai.com/python/py_data_structure/python_graphs.html


使用python字典数据类型轻松呈现图。 5 way to represent a network 王道书


```python
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.getVertices())

```













## 1.1. networkx
https://www.osgeo.cn/networkx/tutorial.html zh-cn


https://networkx.org/documentation/stable/ english















## 1.2. others


package pip install 


interactive with  *.dot











