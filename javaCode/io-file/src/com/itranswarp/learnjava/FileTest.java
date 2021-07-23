package com.itranswarp.learnjava;

import java.io.*;

public class FileTest {

	public static void main0(String[] args) {
		// Windows: C:\\Users 在Java字符串中需要用\\表示一个\; Linux: /usr/bin/javac
		File f = new File("C:\\Users\\pactera\\Downloads\\Documents\\setting.properties");
		System.out.println(f);
		System.out.println(File.separator); // 根据当前平台打印"\"或"/"
	}
	
    public static void main(String[] args) throws IOException {
        File f1 = new File("C:\\Windows");
        File f2 = new File("C:\\Windows\\notepad.exe");
        File f3 = new File("C:\\Windows\\nothing");
        System.out.println(f1+" "+String.valueOf(f1.isFile()));
        System.out.println(f1.isDirectory());
        System.out.println(f2.isFile());
        System.out.println(f2.isDirectory());
        System.out.println(f3.isFile());
        System.out.println(f3.isDirectory());
    }

}
