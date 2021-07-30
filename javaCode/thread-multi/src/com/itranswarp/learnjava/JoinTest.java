package com.itranswarp.learnjava;

public class JoinTest {
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(() -> {
            System.out.println("hello");
        });
        System.out.println("start");
        t.start();
        t.join(); // 等待t线程结束后再继续运行
        System.out.println("end");
    }
}
