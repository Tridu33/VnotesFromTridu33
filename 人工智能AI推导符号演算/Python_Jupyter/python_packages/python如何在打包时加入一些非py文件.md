# python如何在打包时加入一些非py文件








python如何在打包时加入一些非py文件? - marsggbo的回答 - 知乎


可以看到只有py文件被打包了，而yaml文件都被丢掉了，为了解决这个问题，你需要创建一个MANIFEST.in文件，然后输入以下内容recursive-include myapp/configs *.yaml这一行代码的作用是去递归地提取出 myapp/configs路径下的所有yaml文件，当然如果不需要递归的话，你可以把recursive-include改成include。现在我们重新执行打包命令python setup.py sdist bdist_wheel这个时候所有yaml文件也成功打包好了

作者：marsggbo
链接：https://www.zhihu.com/question/59479536/answer/2445883324
