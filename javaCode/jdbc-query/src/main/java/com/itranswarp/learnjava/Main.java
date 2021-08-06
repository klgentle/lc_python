package com.itranswarp.learnjava;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * App entry for Maven project.
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) throws Exception {
		List<Student> students = queryStudents();
		students.forEach(System.out::println);
	}

	static List<Student> queryStudents() throws SQLException {
		List<Student> students = new ArrayList<>();
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn
					.prepareStatement("SELECT * FROM students WHERE grade = ? AND score >= ?")) {
				ps.setInt(1, 2); // 第一个参数 2
				ps.setInt(2, 80); // 第二个参数 80
				try (ResultSet rs = ps.executeQuery()) {
					while (rs.next()) {
						students.add(extractRow(rs));
					}
				}
			}
		}
		return students;
	}

	static Student extractRow(ResultSet rs) throws SQLException {
		var std = new Student();
		std.setId(rs.getLong("id"));
		std.setName(rs.getString("name"));
		std.setGender(rs.getBoolean("gender"));
		std.setGrade(rs.getInt("grade"));
		std.setScore(rs.getInt("score"));
		return std;
	}

//	static final String jdbcUrl = "jdbc:mysql://localhost/learnjdbc?useSSL=false&characterEncoding=utf8";  // mysql 5.*
	static final String jdbcUrl = "jdbc:mysql://localhost/learnjdbc?useSSL=false&characterEncoding=utf8&allowPublicKeyRetrieval=true&serverTimezone=UTC";
	static final String jdbcUsername = "learn";
	static final String jdbcPassword = "learnpassword";
}
