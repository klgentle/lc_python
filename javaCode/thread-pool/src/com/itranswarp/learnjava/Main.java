package com.itranswarp.learnjava;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {
	public static void main(String[] args) {
		ExecutorService es = Executors.newFixedThreadPool(4);
		for (int i = 0; i < 6; i++) {
			es.submit(new Task("" + i));
		}
		es.shutdown();
	}
}

class Task implements Runnable {

	private final String name;

	public Task(String name) {
		this.name = name;
	}

	@Override
	public void run() {
		System.out.println("start task " + name);
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
		}
		System.out.println("end task " + name);
	}
}
