# 台湾SVM包

台湾大 学林智仁教授等开发的的 SVM 开源代码包 LIBSVM


主页
https://www.csie.ntu.edu.tw/~cjlin/libsvm/




仓库 

https://github.com/cjlin1/libsvm


镜像：




https://gitee.com/dengly/libsvm



## 文档下载

-   Chang C C, Lin C J. LIBSVM: A library for Support Vector-Machines. [https://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf](https://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf)




    
-   Hsu C W, Chang C C, Lin C J. A Pratical Guide to Support Vector Classification. [https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf](https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf)

















## 笔记





如何学习SVM（支持向量机）以及改进实现SVM算法程序？ - 韦易笑的回答 - 知乎 https://www.zhihu.com/question/31211585/answer/640501555








```__init__.py```



LIBSVM接口函数在**svmutil.py**文件中，按照源码顺序依次是：

-   `svm_read_problem(data_file_name)`  
    从文本文件中读取数据，数据的格式为：  
    `label index1:value1 index2:value2 ...`  
    返回训练所用的`y`和`x`，使用示例：  
    **`y, x = svm_read_problem('data.txt')`**  
    假定文件中数据如下：  
    `1 1:1.1 2:1.2 3:1.3 4:1.4`  
    `-1 1:-1.1 2:-1.2 3:-1.3 4:-1.4`  
    则`y=[1.0, -1.0]`，  
    `x=[{1: 1.1, 2: 1.2, 3: 1.3, 4: 1.4}, {1: -1.1, 2: -1.2, 3: -1.3, 4: -1.4}]`。
    
-   `svm_load_model(model_file_name)`  
    从文件中读取SVM模型。
    
-   `svm_save_model(model_file_name, model)`  
    将SVM模型保存到文件中。
    
-   `evaluations(ty, pv)`  
    `ty`即训练的数据`y`，  
    `pv`即预测的`y`值。  
    返回`(准确率, 均方误差, 均方相关系数)`这样一个元组，使用示例：  
    `ACC, MSE, SCC = evaluations(y, pred_labels)`。
    
-   `svm_train(arg1, arg2=None, arg3=None)`  
    调用有以下几种形式：  
    `svm_train(y, x [, options]) -> model | ACC | MSE`  
    `svm_train(prob [, options]) -> model | ACC | MSE`  
    `svm_train(prob, param) -> model | ACC | MSE`  
    如果使用了交叉验证，`epsilon-SVR`和`nu-SVR`返回`MSE`，其他返回`ACC`；没有使用交叉验证就返回`model`。  
    后两种调用中出现的`prob`参数是对应`svm.py`文件中的`svm_problem`类型，  
    生成方法为：`prob = svm_problem(y, x)`。  
    最后一种调用方式中出现的`param`参数对应`svm.py`中的`svm_parameter`类型，  
    生成方法为：`param = svm_parameter('-t 0 -c 1')`。  
    `options`类似于linux命令中的参数输入方式，有以下选项：
    
    -   `-s` SVM的类型，默认值为`0`  
        `0 -- C-SVC`  
        `1 -- nu-SVC`  
        `2 -- one-class SVM`  
        `3 -- epsilon-SVR`  
        `4 -- nu-SVR`
        
    -   `-t` 核函数的类型，默认值为`2`  
        `0 -- 线性: u'*v`  
        `1 -- 多项式: (gamma*u'*v + coef0)^degree`  
        `2 -- 径向基: exp(-gamma*|u-v|^2)`  
        `3 -- sigmoid: tanh(gamma*u'*v + coef0)`  
        `4 -- precomputed kernel`，核函数值存储于`training_set_file`中
        
    -   `-d` degree的值，默认为`3`；
        
    -   `-g` gamma的值，默认`1/num_features`；
        
    -   `-r` coef0的值，默认为`0`；
        
    -   `-c` C-SVC, epsilon-SVR, and nu-SVR的cost，默认值为`1`；
        
    -   `-n` nu-SVC, one-class SVM, and nu-SVR中的nu，默认值为`0.5`；
        
    -   `-p` epsilon-SVR的loss function中的epsilon参数，默认值`0.1`；
        
    -   `-m` 缓冲内存大小，单位MB，默认值`100`；
        
    -   `-e` 终止判据的容忍值，默认值`0.001`；
        
    -   `-h` 是否使用收缩启发式算法(shrinking heuristics)，取值0或1，默认值为`0`；
        
    -   `-b` 是否估算正确概率，取值0或1，默认值为`0`；
        
    -   `-wi` C-SVC中第i个特征的Cost参数；
        
    -   `-v` 交叉验证；
        
    -   `-q` 静默方式，无输出。
        
-   `svm_predict(y, x, m, options="")`  
    `y`、`x`对应测试数据，`m`即训练好的model，`options`支持`-b`和`-q`。  
    调用语法：  
    `p_labs, p_acc, p_vals = svm_predict(y, x, model [,'predicting_options'])`  
    返回预测的标签，(准确率, 均方误差, 均方相关系数)元组，以及`-b 1`参数时返回判断系数。
    

> **Tips**：  
> `svm_train(y, x [, options])`这种形式的调用，`x`除了字典形式以外，如：  
> `x = [{1: 1.1, 2: 1.2, 3: 1.3, 4: 1.4}, {1: -1.1, 2: -1.2, 3: -1.3, 4: -1.4}]`  
> 也可以是如下形式，  
> `x = [[1.1, 1.2, 1.3, 1.4], [-1.1, -1.2, -1.3, -1.4]]`  
> `svm_train`会调用`svm.py`文件中`svm_problem`类对`y`和`x`进行包装，`svm_problem`类又会调用`gen_svm_nodearray`函数对`x`进行处理，该函数可以处理`x`两种情形的输入。

  
  
作者：忆霜晨  
链接：https://www.jianshu.com/p/bcc999fc2c8b#fn2  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

### 用法总结

用法总结 https://www.jianshu.com/p/e9cd040de6ce



好看排版： [https://www.cnblogs.com/Finley/p/5329417.html](https://www.cnblogs.com/Finley/p/5329417.html)













## 分析























































