







# java官方日志工具









JDK Logger最大的优点就是不需要任何类库的支持，只要有Java的运行环境就可以使用。相对于其他的日志框架，JDK自带的日志可谓是鸡肋，无论易用性，功能还是扩展性都要稍逊一筹，所以在商业系统中很少直接使用。

```
import java.util.logging.Level;
import java.util.logging.Logger;
 
public class LogJDKTest {
       private static Logger log = Logger.getLogger(LogJDKTest.class.toString());
 
       public static void main(String[] args) {
              // all→finest→finer→fine→config→info→warning→server→off
              // 级别依次升高，后面的日志级别会屏蔽之前的级别
              log.setLevel(Level.INFO);
              log.finest("finest");
              log.finer("finer");
              log.fine("fine");
              log.config("config");
              log.info("info");
              log.warning("warning");
              log.severe("server");
       }
}
```





























