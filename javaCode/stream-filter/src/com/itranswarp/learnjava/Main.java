package com.itranswarp.learnjava;

import java.util.List;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) {
		List<Person> persons = List.of(new Person("小明", 88), new Person("小黑", 62), new Person("小白", 45),
				new Person("小黄", 78), new Person("小红", 99), new Person("小林", 58));
		// 请使用filter过滤出及格的同学，然后打印名字:
		persons.stream();
	}
}

class Person {
	String name;
	int score;

	Person(String name, int score) {
		this.name = name;
		this.score = score;
	}
}