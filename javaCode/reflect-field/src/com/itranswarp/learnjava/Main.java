package com.itranswarp.learnjava;

//reflection
import java.lang.reflect.Field;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) throws NoSuchFieldException, SecurityException, IllegalArgumentException, IllegalAccessException {
		String name = "Xiao Ming";
		int age = 20;
		Person p = new Person();
		// TODO: 利用反射给name和age字段赋值:
		Class c = p.getClass();
		Field fname = c.getDeclaredField("name"); // 加引号
		fname.setAccessible(true);
		fname.set(p, name);
		
		Field fage = c.getDeclaredField("age");
		fage.setAccessible(true);
		fage.set(p, age);
		System.out.println(p.getName()); // "Xiao Ming"
		assert p.getName().equals(name);
		System.out.println(p.getAge()); // 20
		assert p.getAge() == age;
	}
}
