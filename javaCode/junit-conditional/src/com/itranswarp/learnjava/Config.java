package com.itranswarp.learnjava;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Config {

	public String getConfigFile(String filename) {
		String os = System.getProperty("os.name").toLowerCase();
		if (os.contains("win")) {
			return "C:\\" + filename;
		}
		if (os.contains("mac") || os.contains("linux") || os.contains("unix")) {
			return "/usr/local/" + filename;
		}
		throw new UnsupportedOperationException();
	}
}
