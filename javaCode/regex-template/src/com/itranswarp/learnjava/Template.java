package com.itranswarp.learnjava;

import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Template {

	final String template;
	final Pattern pattern = Pattern.compile("\\$\\{(\\w+)\\}");

	public Template(String template) {
		this.template = template;
	}

	public String render(Map<String, Object> data) {
		StringBuffer sb = new StringBuffer();
//		for (String key : data.keySet()) {
//		}
		Matcher m = pattern.matcher(template);
		while (m.find()) {
			m.appendReplacement(sb, String.valueOf(data.get(m.group(1)))); // 循环时一直是group(1)
		}
		m.appendTail(sb);


		return sb.toString();
	}

}