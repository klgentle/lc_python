package com.itranswarp.learnjava;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Time {

	/**
	 * 从"21:59:59"中提取时，分，秒，否则抛出IllegalArgumentException
	 */
	public static int[] parseTime(String s) {
		// FIXME:
		int[] res = new int[3];
		Pattern pattern = Pattern.compile("([0-2]\\d):([0-5]\\d):([0-5]\\d)");
		if (s == null || s.length() < 8 || s.substring(0, 2).equals("24") || s.substring(3, 5).equals("60")
				|| s.substring(6, 8).equals("60")) {
			throw new IllegalArgumentException();
		}

		try {
			Matcher matcher = pattern.matcher(s);
			if (matcher.matches()) {
//				String group0 = matcher.group(0);  // 0表示匹配的整个字符串
				String group1 = matcher.group(1);
				String group2 = matcher.group(2);
				String group3 = matcher.group(3);
//				System.out.println(group1);
				res[0] = group1.charAt(0) == '0' ? Integer.valueOf(group1.substring(1)) : Integer.valueOf(group1);
				res[1] = group2.charAt(0) == '0' ? Integer.valueOf(group2.substring(1)) : Integer.valueOf(group2);
				res[2] = group3.charAt(0) == '0' ? Integer.valueOf(group3.substring(1)) : Integer.valueOf(group3);
			}
		} catch (IllegalArgumentException e) {
			e.printStackTrace();
		}
		return res;
	}

}
