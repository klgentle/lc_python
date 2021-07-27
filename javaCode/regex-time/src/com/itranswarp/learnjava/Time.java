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
		if (s == null || s.length() < 8) {
			throw new IllegalArgumentException();
		}

		Pattern pattern = Pattern.compile("([0-1]\\d|[0-2][0-3]):([0-5]\\d):([0-5]\\d)");
		Matcher matcher = pattern.matcher(s);

		if (matcher.matches()) {
			return new int[] { Integer.valueOf(matcher.group(1)), Integer.valueOf(matcher.group(2)),
					Integer.valueOf(matcher.group(3)) };
		} else {
			throw new IllegalArgumentException();
		}
	}

}
