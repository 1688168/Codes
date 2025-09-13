# <center><b><span style="color:orange">Runnable Pattern</span></b></center>

> # <b><span style="color:purple">Patterns</span></b>

> ### <b><span style="color:green">Java 7 Pattern</span></b>
Runnable runnable = new Runnable(){
    public void run(){
        String name = Thread.currentThread().getName();
        System.outprintln("I am running in thread " + name);
    }
}

> ### <b><span style="color:green">Java 8 Pattern</span></b>

Runnable runnable = () -> {
    String name = Thread.currentThread().getName();
    System.outprintln("I am running in thread " + name);
}

Thread thread = new Thread(runnable);
thread.start();


