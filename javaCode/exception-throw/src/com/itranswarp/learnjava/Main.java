package com.itranswarp.learnjava;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) {
		System.out.println(tax(2000, 0.1));
		try {
			System.out.println(tax(-200, 0.1));
		} catch (IllegalArgumentException e){
			e.printStackTrace();
		} finally {
			System.out.println("-200 end.");
		}
		try {
			System.out.println(tax(2000, -0.1));
		} catch (IllegalArgumentException e){
			e.printStackTrace();
		}finally {
			System.out.println("-0.1 end.");
		}
	}

	static double tax(int salary, double rate) {
		// TODO: 如果传入的参数为负，则抛出 IllegalArgumentException
		if (salary < 0 || rate < 0) {
			throw new IllegalArgumentException();
		}
		return salary * rate;
	}
}
