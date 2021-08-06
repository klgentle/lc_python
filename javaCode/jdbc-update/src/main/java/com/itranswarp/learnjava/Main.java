package com.itranswarp.learnjava;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * App entry for Maven project.
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) throws Exception {
		queryStudents().forEach(System.out::println);
		System.out.println("insert new student...");
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn
					.prepareStatement("INSERT INTO students (name, gender, grade, score) VALUES (?, ?, ?, ?)")) {
				ps.setString(1, "大白");
				ps.setBoolean(2, true);
				ps.setInt(3, 3);
				ps.setInt(4, 97);
				int n = ps.executeUpdate();
				System.out.println(n + " inserted.");
			}
		}
		System.out.println("insert new student and return id...");
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn.prepareStatement(
					"INSERT INTO students (name, gender, grade, score) VALUES (?, ?, ?, ?)",
					Statement.RETURN_GENERATED_KEYS // 返回数据库自动生成的key
			)) {
				ps.setString(1, "老王");
				ps.setBoolean(2, true);
				ps.setInt(3, 3);
				ps.setInt(4, 99);
				int n = ps.executeUpdate();
				long id = 0;
				try (ResultSet rs = ps.getGeneratedKeys()) {
					if (rs.next()) {
						id = rs.getLong(1);
					}
				}
				System.out.println(n + " inserted. id = " + id);
			}
		}
		System.out.println("update student...");
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn.prepareStatement("UPDATE students set score = ? WHERE name = ?")) {
				ps.setInt(1, 99);
				ps.setString(2, "小贝");
				int n = ps.executeUpdate();
				System.out.println(n + " updated.");
			}
		}
		System.out.println("update student2...");
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn.prepareStatement("UPDATE students set family = ? WHERE family is ?")) {
				ps.setString(1, "kl");
				ps.setObject(2, null);  // null 作为 Object 
				int n = ps.executeUpdate();
				System.out.println(n + " updated.");
			}
		}
		System.out.println("delete student...");
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn.prepareStatement("DELETE FROM students WHERE score < ?")) {
				ps.setInt(1, 80);
				int n = ps.executeUpdate();
				System.out.println(n + " deleted.");
			}
		}
		queryStudents().forEach(System.out::println);
	}

	static List<Student> queryStudents() throws SQLException {
		List<Student> students = new ArrayList<>();
		try (Connection conn = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)) {
			try (PreparedStatement ps = conn.prepareStatement("SELECT * FROM students")) {
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
		std.setFamily(rs.getString("family"));
		return std;
	}

//	static final String jdbcUrl = "jdbc:mysql://localhost/learnjdbc?useSSL=false&characterEncoding=utf8";  // mysql 5.*
	static final String jdbcUrl = "jdbc:mysql://localhost/learnjdbc?useSSL=false&characterEncoding=utf8&allowPublicKeyRetrieval=true&serverTimezone=UTC";
	static final String jdbcUsername = "learn";
	static final String jdbcPassword = "learnpassword";
}
