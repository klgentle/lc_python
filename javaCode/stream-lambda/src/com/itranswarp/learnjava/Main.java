package com.itranswarp.learnjava;

import java.util.Arrays;
import java.util.Comparator;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) {
		String[] array = new String[] { "apple", "Orange", "banana", "Lemon" };
		// 请使用忽略大小写排序，并改写为Lambda表达式:
		Arrays.sort(array, new Comparator<>() {
			@Override
			public int compare(String o1, String o2) {
				return o1.compareTo(o2);
			}
		});
		System.out.println(String.join(", ", array));
	}
}
