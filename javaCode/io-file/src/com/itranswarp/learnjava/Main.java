package com.itranswarp.learnjava;

import java.io.File;
import java.io.IOException;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {	
	public static void main(String[] args) throws IOException {
		File currentDir = new File(".");
		listDir(currentDir.getCanonicalFile(), 0);
	}

	static void listDir(File dir, int n) {
		// TODO: 递归打印所有文件和子文件夹的内容
		File[] fs = dir.listFiles();
		if (fs != null) {
			for (File f : fs) {
				for (int i = 1; i <= n; i++) {
					System.out.print("    ");
				}
				System.out.println(f.getName());
				if (f.isDirectory()) {
					listDir(f, n+1);
				}
			}
		}
	}
}
