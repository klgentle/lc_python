package com.itranswarp.learnjava;

import java.io.*;
import java.nio.file.*;

public class TestPath {

	public static void main(String[] args) throws IOException {
		Path p1 = Paths.get(".", "project", "study"); // 构造一个Path对象
		System.out.println(p1);
		Path p2 = p1.toAbsolutePath(); // 转换为绝对路径
		System.out.println(p2);
		Path p3 = p2.normalize(); // 转换为规范路径
		System.out.println(p3);
		File f = p3.toFile(); // 转换为File对象
		System.out.println(f);
		for (Path p : Paths.get("..").toAbsolutePath()) { // 可以直接遍历Path
			System.out.println("  " + p);
		}
	}

}
