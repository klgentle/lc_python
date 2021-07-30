package com.itranswarp.learnjava;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.Security;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {
	public static void main(String[] args) throws Exception {
		// 注册BouncyCastle:
		Security.addProvider(new BouncyCastleProvider());
		// 按名称正常调用:
		MessageDigest md = MessageDigest.getInstance("RipeMD160");
		md.update("HelloWorld".getBytes("UTF-8"));
		byte[] result = md.digest();
		System.out.println(new BigInteger(1, result).toString(16));
	}
}
