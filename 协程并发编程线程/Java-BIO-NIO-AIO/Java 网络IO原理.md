# Java 网络IO原理

## BIO 网络原理 

### 使用示例一  普通BIO

```java
ServerSocket serverSocket = new ServerSocket(DEFAULT_PORT, BACK_LOG, null);
System.out.println("启动服务器");
for (; ; ) {
    Socket socket = serverSocket.accept();
    System.out.println(socket.getRemoteSocketAddress());
    OutputStream outputStream = socket.getOutputStream();
    BufferedWriter bufferedWriter = buildBufferedWriter(outputStream);
    doSomeWork();
    bufferedWriter.write(buildHttpResp());
    bufferedWriter.flush();
}
```

### 使用示例二    普通BIO + 线程池

```java
ServerSocket serverSocket = new ServerSocket(DEFAULT_PORT, BACK_LOG, null);
System.out.println("启动服务器");
ThreadPoolExecutor threadPoolExecutor = buildThreadPoolExecutor();
for (; ; ) {
    Socket socket = serverSocket.accept();
    threadPoolExecutor.execute(() -> {
        OutputStream outputStream;
        BufferedWriter bufferedWriter;
        try {
            System.out.println(socket.getRemoteSocketAddress());
            outputStream = socket.getOutputStream();
            bufferedWriter = buildBufferedWriter(outputStream);
            doSomeWork();
            bufferedWriter.write(buildHttpResp());
            bufferedWriter.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    });
}
```

### 详细原理![image-20210523211834411](C:\Users\hj\AppData\Roaming\Typora\typora-user-images\image-20210523211834411.png)

thread-based architecture（基于线程的架构），通俗的说就是：多线程并发模式，一个连接一个线程，服务器每当收到客户端的一个请求， 便开启一个独立的线程来处理。

这种模式一定程度上极大地提高了服务器的吞吐量，由于在不同线程中，之前的请求在read阻塞以后，不会影响到后续的请求。**但是**，仅适用于于并发量不大的场景，因为：

- 线程需要占用一定的内存资源
- 创建和销毁线程也需一定的代价
- 操作系统在切换线程也需要一定的开销
- 线程处理I/O，在等待输入或输出的这段时间处于空闲的状态，同样也会造成cpu资源的浪费

## NIO 网络原理

### 使用示例一  普通NIO

```java
ServerSocketChannel serverSocketChannel = ServerSocketChannel.open();
serverSocketChannel.bind(new InetSocketAddress(DEFAULT_PORT), BACK_LOG);
System.out.println("启动服务器");
for (; ; ) {
    SocketChannel socketChannel = serverSocketChannel.accept();
    System.out.println(socketChannel.getRemoteAddress());
    String resp = buildHttpResp();
    doSomeWork();
    socketChannel.write(ByteBuffer.wrap(resp.getBytes()));
}
```

### 使用示例二  Selector+NIO

```java
ServerSocketChannel serverSocketChannel = ServerSocketChannel.open();
serverSocketChannel.configureBlocking(false);
serverSocketChannel.bind(new InetSocketAddress(DEFAULT_PORT), BACK_LOG);
Selector selector = Selector.open();
serverSocketChannel.register(selector, SelectionKey.OP_ACCEPT);
System.out.println("启动服务器");
for (; ; ) {
    selector.select();
    Set<SelectionKey> selectionKeys = selector.selectedKeys();
    Iterator<SelectionKey> iterator = selectionKeys.iterator();
    while (iterator.hasNext()) {
        SelectionKey next = iterator.next();
        if (next.isAcceptable()) {
            ServerSocketChannel serverSockChannel = (ServerSocketChannel) next.channel();
            SocketChannel acceptSocketChannel = serverSockChannel.accept();
            System.out.println(acceptSocketChannel.getRemoteAddress());
            acceptSocketChannel.configureBlocking(false);
            acceptSocketChannel.register(selector, SelectionKey.OP_WRITE);
        }
        if (next.isWritable()) {
            SocketChannel socketChannel = (SocketChannel) next.channel();
            String resp = buildHttpResp();
            try {
                doSomeWork();
                socketChannel.write(ByteBuffer.wrap(resp.getBytes()));
            } catch (Exception e) {
            }
        }
        iterator.remove();
    }

}
```

### 详细原理

![image-20210523212305517](C:\Users\hj\AppData\Roaming\Typora\typora-user-images\image-20210523212305517.png)

Reactor的单线程模式的单线程主要是针对于I/O操作而言，也就是所以的I/O的accept()、read()、write()以及connect()操作都在一个线程上完成的。

但在目前的单线程Reactor模式中，不仅I/O操作在该Reactor线程上，连非I/O的业务操作也在该线程上进行处理了，这可能会大大延迟I/O请求的响应。所以我们应该将非I/O的业务逻辑操作从Reactor线程上卸载，以此来加速Reactor线程对I/O请求的响应。

### 使用示例三：多Selector + NIO 

```java
private static final int POLLER_NUM = Runtime.getRuntime().availableProcessors() * 2;
private static Poller[] pollers;

public static ServerSocketChannel createServerSocketChannel() throws Exception {
    ServerSocketChannel serverSocketChannel = ServerSocketChannel.open();
    serverSocketChannel.configureBlocking(true);
    serverSocketChannel.bind(new InetSocketAddress(DEFAULT_PORT), BACK_LOG);
    return serverSocketChannel;
}

public static void initPoller() throws IOException {
    pollers = new Poller[POLLER_NUM];
    for (int i = 0; i < pollers.length; i++) {
        Poller poller = new Poller();
        poller.init();
        pollers[i] = poller;
    }
}

public static void startPoller() {
    for (int i = 0; i < pollers.length; i++) {
        pollers[i].start();
    }
}

public static class Poller extends Thread {
    private Selector selector;
    private BlockingQueue<SocketChannel> socketChannelBlockingQueue = new LinkedBlockingQueue<>();
    private AtomicBoolean atomicBoolean = new AtomicBoolean();

    @Override
    public void run() {
        for (; ; ) {
            try {
                SocketChannel socketChannel = socketChannelBlockingQueue.poll();
                if (socketChannel != null) {
                    socketChannel.configureBlocking(false);
                    doSomeWork();
                    String resp = buildHttpResp();
                    socketChannel.register(selector, SelectionKey.OP_WRITE, ByteBuffer.wrap(resp.getBytes()));

                }
                atomicBoolean.set(true);
                selector.select(1000);
                Set<SelectionKey> selectionKeys = selector.selectedKeys();
                Iterator<SelectionKey> iterator = selectionKeys.iterator();
                while (iterator.hasNext()) {
                    SelectionKey next = iterator.next();
                    if (next.isWritable()) {
                        SocketChannel sc = (SocketChannel) next.channel();

                        try {
                            sc.write((ByteBuffer) next.attachment());
                        } catch (Exception e) {
                        }
                    } else {
                        System.out.println("未知SelectionKey");
                    }
                    iterator.remove();
                }
            } catch (Exception e) {
            }
        }
    }

    public void init() throws IOException {
        selector = Selector.open();
    }

    public void addSocketChannel(SocketChannel socketChannel) {
        try {
            socketChannelBlockingQueue.put(socketChannel);
            if (atomicBoolean.get()) {
                selector.wakeup();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {
        ServerSocketChannel serverSocketChannel = createServerSocketChannel();
        System.out.println("启动服务器");
        initPoller();
        startPoller();
        long count = 0;
        int m = pollers.length - 1;
        for (; ; ) {
            SocketChannel socketChannel = serverSocketChannel.accept();
            System.out.println(socketChannel.getRemoteAddress());
            pollers[(int) (count++ & m)].addSocketChannel(socketChannel);
        }
    }
```

### 详细原理

![image-20210523212500056](C:\Users\hj\AppData\Roaming\Typora\typora-user-images\image-20210523212500056.png)

与单线程模式不同的是，添加了一个**工作者线程池**，并将非I/O操作从Reactor线程中移出转交给工作者线程池（Thread Pool）来执行。这样能够提高Reactor线程的I/O响应，不至于因为一些耗时的业务逻辑而延迟对后面I/O请求的处理。

在工作者线程池模式中，虽然非I/O操作交给了线程池来处理，但是**所有的I/O操作依然由Reactor单线程执行**，在高负载、高并发或大数据量的应用场景，依然较容易成为瓶颈。所以，对于Reactor的优化，又产生出下面的多线程模式。

### 使用示例四   多Selector + NIO + 线程池

```java
private static final int POLLER_NUM = 2;
private static Poller[] pollers;
private static ThreadPoolExecutor poolExecutor = new ThreadPoolExecutor(500, 500,
                                                                        0L, TimeUnit.MILLISECONDS,
                                                                        new SynchronousQueue<>(), new ThreadPoolExecutor.CallerRunsPolicy());
;

public static ServerSocketChannel createServerSocketChannel() throws Exception {
    ServerSocketChannel serverSocketChannel = ServerSocketChannel.open();
    serverSocketChannel.configureBlocking(true);
    serverSocketChannel.bind(new InetSocketAddress(DEFAULT_PORT), BACK_LOG);
    return serverSocketChannel;
}

public static void initPoller() throws IOException {
    pollers = new Poller[POLLER_NUM];
    for (int i = 0; i < pollers.length; i++) {
        Poller poller = new Poller();
        poller.init();
        pollers[i] = poller;
    }
}

public static void startPoller() {
    for (int i = 0; i < pollers.length; i++) {
        pollers[i].start();
    }
}

public static class Poller extends Thread {
    private Selector selector;
    private BlockingQueue<SocketChannel> socketChannelBlockingQueue = new LinkedBlockingQueue<>();
    private AtomicBoolean atomicBoolean = new AtomicBoolean();

    @Override
    public void run() {
        for (; ; ) {
            try {
                for (; ; ) {
                    SocketChannel socketChannel = socketChannelBlockingQueue.poll();
                    if (socketChannel != null) {
                        poolExecutor.execute(() -> {
                            try {
                                socketChannel.configureBlocking(false);
                                doSomeWork();
                                String resp = buildHttpResp();
                                socketChannel.register(selector, SelectionKey.OP_WRITE, ByteBuffer.wrap(resp.getBytes()));
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                        });
                        continue;
                    }
                    break;
                }
                atomicBoolean.set(true);
                selector.select(1000);
                Set<SelectionKey> selectionKeys = selector.selectedKeys();
                Iterator<SelectionKey> iterator = selectionKeys.iterator();
                while (iterator.hasNext()) {
                    SelectionKey next = iterator.next();
                    if (next.isWritable()) {
                        SocketChannel sc = (SocketChannel) next.channel();

                        try {
                            sc.write((ByteBuffer) next.attachment());
                        } catch (Exception e) {
                        }
                    } else {
                        System.out.println("未知SelectionKey");
                    }
                    iterator.remove();
                }
            } catch (Exception e) {
            }
        }
    }

    public void init() throws IOException {
        selector = Selector.open();
    }

    public void addSocketChannel(SocketChannel socketChannel) {
        try {
            socketChannelBlockingQueue.put(socketChannel);
            if (atomicBoolean.get()) {
                selector.wakeup();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {
        ServerSocketChannel serverSocketChannel = createServerSocketChannel();
        System.out.println("启动服务器");
        initPoller();
        startPoller();
        poolExecutor.prestartAllCoreThreads();
        long count = 0;
        int m = pollers.length - 1;
        for (; ; ) {
            SocketChannel socketChannel = serverSocketChannel.accept();
            System.out.println(socketChannel.getRemoteAddress());
            pollers[(int) (count++ & m)].addSocketChannel(socketChannel);
        }
    }
```

### 详细原理

![image-20210523212649643](C:\Users\hj\AppData\Roaming\Typora\typora-user-images\image-20210523212649643.png)

对于多个CPU的机器，为充分利用系统资源，将Reactor拆分为两部分：mainReactor和subReactor。

**mainReactor**负责监听server socket，用来处理网络新连接的建立，将建立的socketChannel指定注册给subReactor，通常**一个线程**就可以处理 ；

**subReactor**维护自己的selector, 基于mainReactor 注册的socketChannel多路分离I/O读写事件，读写网络数据，通常使用**多线程**；

对非I/O的操作，依然转交给工作者线程池（Thread Pool）执行。

此种模型中，每个模块的工作更加专一，耦合度更低，性能和稳定性也大量的提升，支持的可并发客户端数量可达到上百万级别。关于此种模型的应用，目前有很多优秀的框架已经在应用了，比如mina和netty 等。Reactor模式-多线程模式下去掉工作者线程池（Thread Pool），则是Netty中NIO的默认模式。

- mainReactor对应Netty中配置的BossGroup线程组，主要负责接受客户端连接的建立。一般只暴露一个服务端口，BossGroup线程组一般一个线程工作即可
- subReactor对应Netty中配置的WorkerGroup线程组，BossGroup线程组接受并建立完客户端的连接后，将网络socket转交给WorkerGroup线程组，然后在WorkerGroup线程组内选择一个线程，进行I/O的处理。WorkerGroup线程组主要处理I/O，一般设置`2*CPU核数`个线程

## AIO 网络原理

### 使用示例

```java
public static final CountDownLatch EXIT_LATCH = new CountDownLatch(1);
public static AsynchronousServerSocketChannel serverSocketChannel;

public static void createAsynchronousServerSocketChannel(int port) {
    try {
        serverSocketChannel = AsynchronousServerSocketChannel.open();
        serverSocketChannel.bind(new InetSocketAddress(port), BACK_LOG);
    } catch (IOException e) {
        throw new RuntimeException(e);
    }
}


public static class AcceptHandler implements CompletionHandler<AsynchronousSocketChannel, Object> {

    @Override
    public void completed(AsynchronousSocketChannel socketChannel, Object attachment) {
        serverSocketChannel.accept(null, this);
        String resp = buildHttpResp();
        try {
            doSomeWork();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        socketChannel.write(ByteBuffer.wrap(resp.getBytes(StandardCharsets.UTF_8)));
    }

    @Override
    public void failed(Throwable exc, Object attachment) {
        exc.printStackTrace();
    }
}

public static void main(String[] args) {
    System.out.println("start aio server");
    createAsynchronousServerSocketChannel(DEFAULT_PORT);
    serverSocketChannel.accept(null, new AcceptHandler());
    // main thread wait exit
    try {
        System.out.println("wait server close");
        EXIT_LATCH.await();
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    System.out.println("end aio server");
}
```

### 详细原理

异步IO模型。异步IO来自于POSIX AIO规范，它专门提供了能异步IO的读写类函数，如aio_read()，aio_write()等。

使用异步IO函数时，要求指定IO完成时或IO出现错误时的通知方式，通知方式主要分两类：

- 发送指定的信号来通知
- 在另一个线程中执行指定的回调函数

为了帮助理解，这里假设aio_read()的语法如下(真实的语法要复杂的多)：

```
 aio_read(x,y,z,notify_mode,notify_value)
```

其中nofity_mode允许的值有两种：

- 当notify_mode参数的值为`SIGEV_SIGNAL`时，notify_value参数的值为一个信号
- 当notify_mode参数的值为`SIGEV_THREAD`，notify_value参数的值为一个函数，这个函数称为回调函数

当使用异步IO函数时，进程不会因为要执行IO操作而阻塞，而是立即返回。

例如，当进程执行异步IO函数aio_read()时，它会请求内核执行具体的IO操作，当数据已经就绪**且从kernel buffer拷贝到app buffer**后，内核认为IO操作已经完成，于是内核会根据调用异步IO函数时指定的通知方式来执行对应的操作：

- 如果通知模式是信号通知方式(SIGEV_SIGNAL)，则在IO完成时，内核会向进程发送notify_value指定的信号
- 如果通知模式是信号回调方式(SIGEV_THREAD)，则在IO完成时，内核会在一个独立的线程中执行notify_value指定的回调函数

回顾一下信号驱动IO，信号驱动IO要求有另一端主动向文件描述符写入数据，所以它支持像socket、pipe、terminal这类文件描述符，但不支持普通文件IO的文件描述符。

而异步IO则没有这个限制，异步IO操作借助的是那些具有神力的异步函数，只要文件描述符能读写，就能使用异步IO函数来实现异步IO。

所以，异步IO在整个过程中都不会被阻塞。如图：

![img](https://images2017.cnblogs.com/blog/733013/201710/733013-20171003171529536-693464967.png)

看上去异步很好，但是注意，在复制kernel buffer数据到app buffer中时是需要CPU参与的，这意味着不受阻的进程会和异步调用函数争用CPU。以httpd为例，如果并发量比较大，httpd接入的连接数可能就越多，CPU争用情况就越严重，异步函数返回成功信号的速度就越慢。如果不能很好地处理这个问题，异步IO模型也不一定就好。

## Netty 线程模型原理

![image-20210523212911552](C:\Users\hj\AppData\Roaming\Typora\typora-user-images\image-20210523212911552.png)

如上图下侧为Netty Server端,当NettyServer启动时候会创建两个NioEventLoopGroup线程池组，其中boss组用来接受客户端发来的连接，worker组则负责对完成TCP三次握手的连接进行处理；如上图每个NioEventLoopGroup里面包含了多个NioEventLoop，每个NioEventLoop中包含了一个NIO Selector、一个队列、一个线程；其中线程用来做轮询注册到Selector上的Channel的读写事件和对投递到队列里面的事件进行处理。

当NettyServer启动时候会注册监听套接字通道NioServerSocketChannel到boss线程池组中的某一个NioEventLoop管理的Selector上，然后其对应的线程则会负责轮询该监听套接字上的连接请求；当客户端发来一个连接请求时候，boss线程池组中注册了监听套接字的NioEventLoop中的Selector会读取读取完成了TCP三次握手的请求，然后创建对应的连接套接字通道NioSocketChannel，然后把其注册到worker线程池组中的某一个NioEventLoop中管理的一个NIO Selector上，然后该连接套接字通道NioSocketChannel上的所有读写事件都由该NioEventLoop管理。当客户端发来多个连接时候，NettyServer端则会创建多个NioSocketChannel，而worker线程池组中的NioEventLoop是有个数限制的，所以Netty有一定的策略把很多NioSocketChannel注册到不同的NioEventLoop上，也就是每个NioEventLoop中会管理好多客户端发来的连接，然后通过循环轮询处理每个连接的读写事件。

如上图上侧部分为Netty Client部分，当NettyClient启动时候会创建一个NioEventLoopGroup，用来发起请求并对建立TCP三次连接的套接字的读写事件进行处理。当调用Bootstrap的connect方法发起连接请求后内部会创建一个NioSocketChannel用来代表该请求，并且会把该NioSocketChannel注册到NioSocketChannel管理的某个NioEventLoop的Selector上，然后该NioEventLoop的读写事件都有该NioEventLoop负责处理。

Netty之所以说是异步非阻塞网络框架是因为通过NioSocketChannel的write系列方法向连接里面写入数据时候是非阻塞的，马上会返回的，即使调用写入的线程是我们的业务线程，这是Netty通过在ChannelPipeline中判断调用NioSocketChannel的write的调用线程是不是其对应的NioEventLoop中的线程来实现的，如果发现不是则会把写入请求封装为WriteTask投递到其对应的NioEventLoop中的队列里面，然后等其对应的NioEventLoop中的线程轮询连接套接字的读写事件时候捎带从队列里面取出来执行；总结说就是每个NioSocketChannel对应的读写事件都是在其对应的NioEventLoop管理的单线程内执行，对同一个NioSocketChannel不存在并发读写，所以无需加锁处理。

另外当从NioSocketChannel中读取数据时候，并不是使用业务线程来阻塞等待，而是等NioEventLoop中的IO轮询线程发现Selector上有数据就绪时候，通过事件通知方式来通知我们业务数据已经就绪，可以来读取并处理了。

总结一句话就是使用Netty框架进行网络通信时候，当我们发起请求后请求会马上返回，而不会阻塞我们的业务调用线程；如果我们想要获取请求的响应结果，也不需要业务调用线程使用阻塞的方式来等待，而是当响应结果出来时候使用IO线程异步通知业务的方式，可知在整个请求-响应过程中业务线程不会由于阻塞等待而不能干其他事情。

## Tomcat 线程模型原理

![](C:\Users\hj\AppData\Roaming\Typora\typora-user-images\image-20210523213248110.png)

一个或多个Acceptor线程，每个线程都有自己的Selector，Acceptor只负责accept新的连接，一旦连接建立之后就将连接注册到其他Worker线程中。
多个Worker线程，有时候也叫IO线程，就是专门负责IO读写的。一种实现方式就是像Netty一样，每个Worker线程都有自己的Selector，可以负责多个连接的IO读写事件，每个连接归属于某个线程。另一种方式实现方式就是有专门的线程负责IO事件监听，这些线程有自己的Selector，一旦监听到有IO读写事件，并不是像第一种实现方式那样（自己去执行IO操作），而是将IO操作封装成一个Runnable交给Worker线程池来执行，这种情况每个连接可能会被多个线程同时操作，相比第一种并发性提高了，但是也可能引来多线程问题，在处理上要更加谨慎些。tomcat的NIO模型就是第二种。

![image-20210523213416043](C:\Users\hj\AppData\Roaming\Typora\typora-user-images\image-20210523213416043.png)

这张图勾画出了NioEndpoint的大致执行流程图，worker线程并没有体现出来，它是作为一个线程池不断的执行IO读写事件即SocketProcessor（一个Runnable），即这里的Poller仅仅监听Socket的IO事件，然后封装成一个个的SocketProcessor交给worker线程池来处理。下面我们来详细的介绍下NioEndpoint中的Acceptor、Poller、SocketProcessor。
它们处理客户端连接的主要流程如图所示：

图中Acceptor及Worker分别是以线程池形式存在，Poller是一个单线程。注意，与BIO的实现一样，缺省状态下，在server.xml中没有配置<Executor>，则以Worker线程池运行，如果配置了<Executor>，则以基于java concurrent 系列的java.util.concurrent.ThreadPoolExecutor线程池运行。

### Acceptor

接收socket线程，这里虽然是基于NIO的connector，但是在接收socket方面还是传统的serverSocket.accept()方式，获得SocketChannel对象，然后封装在一个tomcat的实现类org.apache.tomcat.util.net.NioChannel对象中。然后将NioChannel对象封装在一个PollerEvent对象中，并将PollerEvent对象压入events queue里。这里是个典型的生产者-消费者模式，Acceptor与Poller线程之间通过queue通信，Acceptor是events queue的生产者，Poller是events queue的消费者。

### Poller

Poller线程中维护了一个Selector对象，NIO就是基于Selector来完成逻辑的。在connector中并不止一个Selector，在socket的读写数据时，为了控制timeout也有一个Selector，在后面的BlockSelector中介绍。可以先把Poller线程中维护的这个Selector标为主Selector。 Poller是NIO实现的主要线程。首先作为events queue的消费者，从queue中取出PollerEvent对象，然后将此对象中的channel以OP_READ事件注册到主Selector中，然后主Selector执行select操作，遍历出可以读数据的socket，并从Worker线程池中拿到可用的Worker线程，然后将socket传递给Worker。整个过程是典型的NIO实现。

### Worker

Worker线程拿到Poller传过来的socket后，将socket封装在SocketProcessor对象中。然后从Http11ConnectionHandler中取出Http11NioProcessor对象，从Http11NioProcessor中调用CoyoteAdapter的逻辑，跟BIO实现一样。在Worker线程中，会完成从socket中读取http request，解析成HttpServletRequest对象，分派到相应的servlet并完成逻辑，然后将response通过socket发回client。在从socket中读数据和往socket中写数据的过程，并没有像典型的非阻塞的NIO的那样，注册OP_READ或OP_WRITE事件到主Selector，而是直接通过socket完成读写，这时是阻塞完成的，但是在timeout控制上，使用了NIO的Selector机制，但是这个Selector并不是Poller线程维护的主Selector，而是BlockPoller线程中维护的Selector，称之为辅Selector。

### Tomcat 并发参数控制

#### acceptCount

文档描述为：
The maximum queue length for incoming connection requests when all possible request processing threads are in use. Any requests received when the queue is full will be refused. The default value is 100.
这个参数就立马牵涉出一块大内容：TCP三次握手的详细过程，这个之后再详细探讨。这里可以简单理解为：连接在被ServerSocketChannel accept之前就暂存在这个队列中，acceptCount就是这个队列的最大长度。ServerSocketChannel accept就是从这个队列中不断取出已经建立连接的的请求。所以当ServerSocketChannel accept取出不及时就有可能造成该队列积压，一旦满了连接就被拒绝了

#### acceptorThreadCount

文档如下描述
The number of threads to be used to accept connections. Increase this value on a multi CPU machine, although you would never really need more than 2. Also, with a lot of non keep alive connections, you might want to increase this value as well. Default value is 1.
Acceptor线程只负责从上述队列中取出已经建立连接的请求。在启动的时候使用一个ServerSocketChannel监听一个连接端口如8080，可以有多个Acceptor线程并发不断调用上述ServerSocketChannel的accept方法来获取新的连接。参数acceptorThreadCount其实使用的Acceptor线程的个数。

#### maxConnections

文档描述如下
The maximum number of connections that the server will accept and process at any given time. When this number has been reached, the server will accept, but not process, one further connection. This additional connection be blocked until the number of connections being processed falls below maxConnections at which point the server will start accepting and processing new connections again. Note that once the limit has been reached, the operating system may still accept connections based on the acceptCount setting. The default value varies by connector type. For NIO and NIO2 the default is 10000. For APR/native, the default is 8192.
Note that for APR/native on Windows, the configured value will be reduced to the highest multiple of 1024 that is less than or equal to maxConnections. This is done for performance reasons. If set to a value of -1, the maxConnections feature is disabled and connections are not counted.
这里就是tomcat对于连接数的一个控制，即最大连接数限制。一旦发现当前连接数已经超过了一定的数量（NIO默认是10000），上述的Acceptor线程就被阻塞了，即不再执行ServerSocketChannel的accept方法从队列中获取已经建立的连接。但是它并不阻止新的连接的建立，新的连接的建立过程不是Acceptor控制的，Acceptor仅仅是从队列中获取新建立的连接。所以当连接数已经超过maxConnections后，仍然是可以建立新的连接的，存放在上述acceptCount大小的队列中，这个队列里面的连接没有被Acceptor获取，就处于连接建立了但是不被处理的状态。当连接数低于maxConnections之后，Acceptor线程就不再阻塞，继续调用ServerSocketChannel的accept方法从acceptCount大小的队列中继续获取新的连接，之后就开始处理这些新的连接的IO事件了。

#### maxThreads

文档描述如下
The maximum number of request processing threads to be created by this Connector, which therefore determines the maximum number of simultaneous requests that can be handled. If not specified, this attribute is set to 200. If an executor is associated with this connector, this attribute is ignored as the connector will execute tasks using the executor rather than an internal thread pool.
这个简单理解就算是上述worker的线程数。他们专门用于处理IO事件，默认是200。