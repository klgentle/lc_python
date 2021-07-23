package com.itranswarp.learnjava;

import java.io.UnsupportedEncodingException;
import java.util.logging.Logger;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) {
		Logger logger = Logger.getLogger(Main.class.getName());
		logger.info("Start process...");
		try {
			"".getBytes("invalidCharsetName");
		} catch (UnsupportedEncodingException e) {
			// TODO: 使用logger.severe()打印异常
			logger.severe("error: " + e.getMessage());
		}

		logger.info("Process end.");
	}
}
