[Runnable pattern]
```java
Runnable task = () -> System.out.println("Hello World!");
Thread thread = new Thread(task);
thread.start();
```