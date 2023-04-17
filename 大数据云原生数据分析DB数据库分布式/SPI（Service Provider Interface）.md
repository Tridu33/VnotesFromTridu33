# SPI（Service Provider Interface）







SPI扩展机制应用场景有很多，比如Common-Logging，JDBC， Dubbo 等等。
https://javaguide.cn/java/basis/spi.html#%E5%AE%9E%E6%88%98%E6%BC%94%E7%A4%BA


在SPI机制选择时，可以考虑使用dubbo实现的SPI机制。




Java 中的 SPI 机制就是在每次类加载的时候会先去找到 class 相对目录下的 META-INF 文件夹下的 services 文件夹下的文件，将这个文件夹下面的所有文件先加载到内存中，然后根据这些文件的文件名和里面的文件内容找到相应接口的具体实现类，找到实现类后就可以通过反射去生成对应的对象，保存在一个 list 列表里面，所以可以通过迭代或者遍历的方式拿到对应的实例对象，生成不同的实现。