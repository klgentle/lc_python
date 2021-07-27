package com.itranswarp.learnjava;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class CopyFile {

	public static void main(String[] args) throws IOException {
		if (args.length != 2) {
			System.err.println("Usage:\n  java CopyFile.java <source> <target>");
			System.exit(1);
		}
		copy(args[0], args[1]);
	}

	static void copy1(String source, String target) throws IOException {
		// 友情提示：测试时请使用无关紧要的文件
		try (InputStreamReader input = new InputStreamReader(new FileInputStream(source), "UTF-8");  // 使用InputStreamReader 指定编码
			 OutputStream out = new FileOutputStream(target))
		{
			// read
			int n;
			StringBuilder sb = new StringBuilder();
			while ((n = input.read()) != -1) {
				sb.append((char) n);
			}
			System.out.println(sb.toString());
			// write
			out.write(sb.toString().getBytes("UTF-8"));
			out.flush(); // 清空缓存
		}
		System.out.println("Copy success!");
	}
	
	static void copy(String source, String target) throws IOException {
		// 友情提示：测试时请使用无关紧要的文件
		try (InputStream input = new FileInputStream(source);
			     OutputStream output = new FileOutputStream(target))
			{
				
			    input.transferTo(output);  // 真简洁啊
			    output.flush(); // 清空缓存
			    System.out.println("复制成功");
			}
	}
}
