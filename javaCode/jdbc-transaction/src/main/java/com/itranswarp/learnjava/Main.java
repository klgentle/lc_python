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
		insertStudents("大黄", true, 3, 100);
		insertStudents("大头", false, 3, 101);
		List<Student> students = queryStudents();
		students.forEach(System.out::println);
	}

	static void insertStudents(String name, boolean gender, int grade, int score) throws SQLException {
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			boolean isAutoCommit = conn.getAutoCommit();
			conn.setAutoCommit(false); // 关闭自动提交事务
			try (PreparedStatement ps = conn
					.prepareStatement("INSERT INTO students (name, gender, grade, score) VALUES (?, ?, ?, ?)")) {
				ps.setString(1, name);
				ps.setBoolean(2, gender);
				ps.setInt(3, grade);
				ps.setInt(4, score);
				int n = ps.executeUpdate();
				System.out.println(n + " inserted.");
			}
			if (score > 100) {
				conn.rollback();
				System.out.println("rollback.");

			} else {
				conn.commit();
				System.out.println("commit.");
			}
			conn.setAutoCommit(isAutoCommit); // 恢复AutoCommit设置
		}
	}

	static List<Student> queryStudents() throws SQLException {
		List<Student> students = new ArrayList<>();
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn
					.prepareStatement("SELECT * FROM students WHERE grade = ? AND score >= ?")) {
				ps.setInt(1, 3); // 第一个参数grade=?
				ps.setInt(2, 90); // 第二个参数score=?
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
