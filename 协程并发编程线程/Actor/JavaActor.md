
https://www.baeldung.com/akka-actors-java 很好的例子
 https://github.com/eugenp/tutorials/tree/master/libraries-5/src/main/java/com/baeldung



https://blog.csdn.net/shenjuntao520/article/details/114591237

最小手写demo

并发之痛 Thread，Goroutine，Actor



Actor最容易理解的博客Go源码实现
https://github.com/gauravsa/go-actor-system


# JavaActor


Akka Actor https://blog.csdn.net/shenjuntao520/article/details/114591237


那么Akka是怎么改进的呢？Akka引入了ActorSystem、ActorRef（Actor引用）、Message Dispatcher（消息分发器）、MailBox。具体的基本流程为：

1.用户创建一个ActorSystem，由他来管理Actor，相当于是Actor的一个文件夹。

2.用户通过ActorSystem来创建一个ActorRef，并将消息发送给ActorRef，这里ActorRef扮演的是个Proxy（代理）的角色。

3.ActorRef把消息发送给Message Dispatcher，这个消息分发器用来把消息分发下去，相当于是个传达室的作用。

4.Message Dispatcher把消息按照顺序保存到目标Actor的MailBox中。可以理解为因为Actor很忙，所以传达室收到报纸后把报纸交给小助手。

5.Message Dispatcher将MailBox放到一个线程中。相当于传达室安排小助手去工作。

5.MailBox按照顺序取出消息，最终把它传递给目标Actor接收的方法中。这一步相当于小助手按照接收的顺序把报纸给到接收人。


---


我们相信Actor内部自动异步处理自己的邮箱中的数据，
实际内部原理要看 https://www.cnblogs.com/Aitozi/p/15704987.html 深入理解Actor框架

```java
import java.util.concurrent.CountDownLatch;
/*
        <dependency>
            <groupId>com.typesafe.akka</groupId>
            <artifactId>akka-actor_2.10</artifactId>
            <version>2.3.16</version>
        </dependency>
        <dependency>
            <groupId>org.scala-lang</groupId>
            <artifactId>scala-actors</artifactId>
            <version>2.11.12</version>
        </dependency>
* */
import akka.actor.UntypedActor;
import akka.actor.ActorRef;
import akka.actor.ActorSystem;
import akka.actor.Props;
import akka.pattern.Patterns;
import scala.concurrent.Future;

class BankActor extends UntypedActor {
    private int count;

    @Override
    public void preStart() throws Exception {
        super.preStart();
        count = 0;
    }

    @Override
    public void onReceive(Object message) {
        // 可以使用枚举或者动态代理类来实现方法调用
        if (message instanceof Command) {
            Command cmd = (Command) message;
            switch (cmd) {
                case ADD:
                    System.out.println("Add 1 from " + count + " to " + ++count);
                    break;
                case MINUS:
                    System.out.println("Minus 1 from " + count + " to " + --count + "");
                    break;
                case GET:
                    System.out.println("Return current count " + getSender());
                    getSender().tell(count, this.getSelf());
                    break;
                default:
                    System.out.println("UnSupport cmd: " + cmd);
            }
        } else {
            System.out.println("Discard unknown message: " + message);
        }
    }
}

enum Command {
    ADD,
    MINUS,
    GET
}


public class ActorDemo {
//  @SneakyThrows
    public static void main(String[] args) throws InterruptedException {
        final ActorSystem actorSystem = ActorSystem.create("actor-system");

        final ActorRef actorRef = actorSystem.actorOf(Props.create(BankActor.class), "bank-actor");

        CountDownLatch addCount = new CountDownLatch(20);
        CountDownLatch minusCount = new CountDownLatch(10);

        Thread addCountT = new Thread(new Runnable() {
            @Override
            public void run() {
                while (addCount.getCount() > 0) {
                    // 仅仅是使用Actor模型的层次上，只需要理解到扔到邮箱通知队列中，
                    actorRef.tell(Command.ADD, null);
                    addCount.countDown();
                }
            }
        });

        Thread minusCountT = new Thread(new Runnable() {
            @Override
            public void run() {
                while (minusCount.getCount() > 0) {
                    actorRef.tell(Command.MINUS, null);
                    minusCount.countDown();
                }
            }
        });

        minusCountT.start();
        addCountT.start();
        minusCount.await();
        addCount.await();

        Future<Object> count = Patterns.ask(actorRef, Command.GET, 1000);
        while (true) {
            if (count.isCompleted()) {
                break;
            }
        }
        System.out.println(count.value());
//        final Timeout timeout = new Timeout(Duration.create(3, TimeUnit.SECONDS));
//        Integer res = (Integer) Await.result(count,timeout.duration());
//        System.out.println(res);
        actorSystem.shutdown();
    }
}
```





























