package com.itranswarp.learnjava;

import java.io.IOException;
import java.util.function.LongSupplier;
import java.util.stream.LongStream;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {
	public static void main(String[] args) throws IOException {
		LongStream fib = LongStream.generate(new FibSupplier());
		// 打印Fibonacci数列：1，1，2，3，5，8，13，21...
		fib.limit(10).forEach(System.out::println);
	}
}

class FibSupplier implements LongSupplier {
	public long getAsLong() {
		return 0;
	}
}
