 
https://mermaid-js.github.io/mermaid/#/n00b-advanced


https://mermaid-js.github.io/mermaid-live-editor/



















新版本mermaid语法上有点问题，&not等特殊标记符号不好使




这里请看纯文本不要看渲染后的结果

# 1. mkdocs-mermaid

看了很多，但是发现：



superfences首先将md文件中```flow以及```sequence区块部分的逻辑代码转换为

```
<pre class="uml-flowchart"><code>
...
</code></pre>

<pre class="uml-sequence-diagram"><code>
...
</code></pre>
```

并插入到最终生成的html文件中，然后umlconvert.js通过flowchart.js、sequence-diagram.js将html页面标签中的uml-flowchart和uml-sequence-diagram部分的逻辑代码转换为流程图以及序列图。

直接在Typora中写HTML代码，Typora中不能看图只能看代码，但是这种情况下Mkdocs生成的html能看到图像：

<pre class="uml-flowchart"><code>
st=>start: Start:>http://www.google.com[blank]
e=>end:>http://www.google.com
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?:>http://www.google.com
io=>inputoutput: catch something...
st->op1->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
</code></pre>

<pre class="uml-sequence-diagram"><code>
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
</code></pre>

直接在Typora中写mermaid标记，mkdocs中不能看图只能看代码，但是这种情况下Typora能看到图像，而vnote只能看到一个，因为js文件的加载和函数命名空间问题之类的：


```flow
st=>start: Start:>http://www.google.com[blank]
e=>end:>http://www.google.com
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?:>http://www.google.com
io=>inputoutput: catch something...
st->op1->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
```

```sequence
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
```




```
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ff0000'}}}%%
        graph TD
          A[Christmas] -->|Get money| B(Go shopping)
          B --> C{Let me think}
          B --> G[/Another/]
          C ==>|One| D[Laptop]
          C -->|Two| E[iPhone]
          C -->|Three| F[fa:fa-car Car]
          subgraph section
            C
            D
            E
            F
            G
          end
```
# 2. 此时的mkdocs配置文件备份


```
# Project information
site_description: ZERO-Starting AI Planning in PDDL-Descripted World
site_author: 'tridu33'
copyright: 'Copyright &copy; 2020 tridu33'
#网页名
site_name: AI Planning in PDDL-Descripted World
site_url : null
#源文件路径
docs_dir: 'docs'
#网页静态文件生成路径
site_dir: 'site'
# 额外信息
extra:
    # 版本号
    version: 0.1.0
# Repository
repo_name: 'PDDL笔记'
repo_url: 'https://github.com/Tridu33/ZERO-Starting-AI-Planning-in-PDDL-Descripted-World'


# 主题
theme: 
    # name: 'readthedocs'
    # name: 'mkdocs'
    #name: 'material'
# Configuration
    name: 'ivory' #'ivory'
    language: 'zh'
    highlightjs: true
    hljs_languages:
        - yaml
        - python



# Customization
extra:
  search:
    language: 'en'
    manifest: 'manifest.webmanifest'
  social:
    - type: 'github'
      link: 'https://github.com/Tridu33/ZERO-Starting-AI-Planning-in-PDDL-Descripted-World'


# Github pages
remote_branch: gh-pages
remote_name: origin

# Google Analytics
google_analytics:
  - 'UA-XXXXXXXX-X'
  - 'auto'

# Extensions 
# markdown扩展markdown_extensions:
markdown_extensions:
  # 参考[MathJax](https://squidfunk.github.io/mkdocs-material/reference/mathjax/)，支持数学公式渲染
  - pymdownx.arithmatex:
      generic: true
    # 参考[Icons + Emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)，执行Markdown Emoji
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
  - pymdownx.caret 
  - pymdownx.critic 
  - pymdownx.details 
  - pymdownx.inlinehilite 
  - pymdownx.magiclink 
  - pymdownx.mark 
  - pymdownx.smartsymbols 
  - pymdownx.superfences 
  - pymdownx.tasklist 
  - pymdownx.tilde
  - admonition 
  - pymdownx.betterem: 
      smart_enable: all 
  - codehilite: 
      guess_lang: false 
      linenums: false 
  - toc: 
      permalink: true 
  - footnotes 
  - meta 
  - def_list 
  - attr_list
  - pymdownx.superfences:
      # make exceptions to highlighting of code:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:mermaid2.fence_mermaid
          #https://squidfunk.github.io/mkdocs-material/reference/diagrams/

#mermaid https://github.com/fralau/mkdocs-mermaid2-plugin#installation
plugins:
  - search:
  - minify:
      minify_html: true

# mathjax https://cdnjs.com/

#z主要是这里导入js文件解析渲染
extra_javascript:
    - js/umlconvert.js
    - js/sequence-loader.js
    - https://unpkg.com/mermaid/dist/mermaid.min.js
    - https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js
    - https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.12.0/underscore-min.js
    - https://cdnjs.cloudflare.com/ajax/libs/js-sequence-diagrams/1.0.6/sequence-diagram-min.js
    - https://cdnjs.cloudflare.com/ajax/libs/flowchart/1.6.5/flowchart.min.js


#nav
nav:
    - Home: index.md
    - 规划界黑话:
      - PDDL进化史:
        - ADL: PlanLanguages/ADL.md
        - STRIPS: PlanLanguages/STRIPS.md
        - PDDL: PlanLanguages/PDDL.md
      - 机器人世界:
        - Golog: PlanLanguages/Golog_ROS.md
    - PDDL使用:
      - 本地环境使用: Usage/LocalSolvers.md
      - 线上求解器使用: Usage/OnlineSolver.md
      - Visual Studio Code使用: Usage/VSCode.md
    - PDDL语法:
      - 语法总览: Syntax/main.md
      - 实例演示: Syntax/samples.md
      - 版本扩展': Syntax/version.md
    - Issue跟踪讨论 : https://github.com/Tridu33/ZERO-Starting-AI-Planning-in-PDDL-Descripted-World/issues



```























