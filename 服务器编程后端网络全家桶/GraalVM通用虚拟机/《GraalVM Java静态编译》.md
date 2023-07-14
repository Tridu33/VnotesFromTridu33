






https://gitee.com/ziyilin/GraalBook 随书代码
pom.xml maven打包依赖到jar中需要配置
```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>3.0.0</version>
                <configuration>
                    <finalName>EncDecCmd</finalName>
                    <archive>
                        <manifest>
                            <mainClass>com.test.EncryptUtilsTest</mainClass>
                        </manifest>
                    </archive>
                    <descriptorRefs>
                        <descriptorRef>
                            jar-with-dependencies
                        </descriptorRef>
                    </descriptorRefs>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
```
Linux默认，Windows不是默认需要这样：
```bash
native-image --no-fallback -jar ./target/Package-jar-with-dependencies.jar
```
# 《GraalVM Java静态编译》 原理与应用

Micronaut框架的greeting-example
https://github.com/codeurjc/micronaut-spring-graal-maven-example/blob/master/README.md 



GraalVM 的 插件 https://graalvm.github.io/native-build-tools/latest/index.html
https://github.com/graalvm/native-build-tools/tree/master/samples

 
- maven 
https://graalvm.github.io/native-build-tools/latest/maven-plugin-quickstart.html
- gradle
https://graalvm.github.io/native-build-tools/latest/gradle-plugin.html



# Spring -Native

https://github.com/spring-attic/spring-native/tree/main/samples 这些是作者例子

合并到Spring Boot 3原生支持
https://docs.spring.io/spring-boot/docs/current/reference/html/native-image.html



https://github.com/mraible/spring-native-examples 油管小众例子

开始使用 Spring Native 的最简单方法可能是访问 start.spring.io ，添加 Spring Native 依赖项，并阅读参考文档。确保正确配置Spring AOT Maven 和 Gradle 插件 


Spring Boot Native最著名的两个例子：
https://github.com/spring-projects/spring-petclinic 
petclinic-jdbc petclinic-jpa
























# 使用Micronaut框架的云原生Java
https://micronaut.io/

https://github.com/micronaut-projects/presentations/tree/master

https://www.jetbrains.com/help/idea/micronaut.html






Micronaut框架为构建基于编译时方法的云原生Java微服务提供了坚实的基础。
与GraalVM Native Image AOT(Ahead-of-Time Compilation)的紧密集成使得应用程序可以轻松转换为本地可执行文件，这具有巨大的优势，特别是对于无服务器和微服务的工作负载。
减少对Java反射、运行时代理生成和动态类加载的使用，带来了性能、内存和启动方面的改进，使Micronaut应用程序的调试和测试变得更加容易。
主动的编译时检查增加了类型的安全性，并通过在构建时而非运行时浮现错误来提高开发人员的工作效率。
一个庞大的模块和集成的生态系统，如用于数据库访问的Micronaut Data，有助于在Micronaut框架内提供进一步的创新。


---



Micronaut Data支持几种不同的数据库和查询格式包括：
https://juejin.cn/post/7125257915006451720
Hibernate和JPA- 你可以使用JPA和Hibernate，Micronaut Data JPA在编译期间计算JPA查询（如上所述）。
JDBC和SQL- 对于那些喜欢原始SQL和简单的数据映射器而不是对象关系映射（ORM）的人来说，Micronaut Data JDBC提供了一个简单的解决方案，可以从关系型数据库读写Java 17+记录和POJOs。
MongoDB- 作为最新增加的功能，Micronaut Data MongoDB直接与MongoDB驱动集成，使用Micronaut Serialization以完全无反射的方式将对象编码到BSON。
R2DBC- 基于Netty，Micronaut框架具有一个反应式、非阻塞式的核心。通过将Micronaut Netty服务器与反应式数据库连接（R2DBC）规范和支持的数据库相结合，你可以编写避免端到端阻塞的SQL应用程序。
Oracle Coherence- 一个用于大规模的分布式数据网格，Coherence的特点是与Micronaut Data的专门集成，以轻松实现由Coherence集群支持的存储库。






---


https://micronaut-projects.github.io/micronaut-grpc/3.0.2/guide/index.html

https://github.com/micronaut-projects/micronaut-grpc/tree/master
Integration between Micronaut and GRPC


 




https://github.com/codeurjc/micronaut-spring-graal-maven-example/tree/master









# substrate VM用java编写共享库文件
.dll等文件样例 https://gitee.com/ziyilin/GraalBook/tree/master/cinterfacetutorial


[CLibrary](https://github.com/oracle/graal/blob/master/substratevm/src/com.oracle.svm.tutorial/src/com/oracle/svm/tutorial/CInterfaceTutorial.java)



























































































































