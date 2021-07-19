package com.itranswarp.learnjava;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) {
		String[] fields = { "name", "position", "salary" };
		String table = "employee";
		String insert = buildInsertSql(table, fields);
		System.out.println(insert);
		System.out.println(
				"INSERT INTO employee (name, position, salary) VALUES (?, ?, ?)".equals(insert) ? "测试成功" : "测试失败");
	}

	static String buildInsertSql(String table, String[] fields) {
		// TODO:请使用StringBuilder构造一个INSERT语句
		StringBuilder s = new StringBuilder(1024);
		s.append("INSERT INTO ")
		 .append(table)
		 .append(" (")
		 .append(String.join(", ", fields))
		 .append(") VALUES (?, ?, ?)");
		return s.toString();
	}

}
