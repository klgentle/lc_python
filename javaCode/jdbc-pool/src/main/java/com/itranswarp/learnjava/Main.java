package com.itranswarp.learnjava;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.sql.DataSource;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

/**
 * App entry for Maven project.
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) throws Exception {
		HikariConfig config = new HikariConfig();
		config.setJdbcUrl(jdbcUrl);
		config.setUsername(jdbcUsername);
		config.setPassword(jdbcPassword);
		config.addDataSourceProperty("cachePrepStmts", "true");
		config.addDataSourceProperty("prepStmtCacheSize", "100");
		config.addDataSourceProperty("maximumPoolSize", "10");
		DataSource ds = new HikariDataSource(config);
		List<Student> students = queryStudents(ds);
		students.forEach(System.out::println);
	}

	static List<Student> queryStudents(DataSource ds) throws SQLException {
		List<Student> students = new ArrayList<>();
		try (Connection conn = ds.getConnection()) { // 在此获取连接
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
		} // 在此“释放”连接
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
