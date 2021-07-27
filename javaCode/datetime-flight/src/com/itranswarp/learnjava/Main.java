package com.itranswarp.learnjava;

import java.time.*;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 * 
 * 某航线从北京飞到纽约需要13小时20分钟，请根据北京起飞日期和时间计算到达纽约的当地日期和时间。
 */
public class Main {
	public static void main(String[] args) {
		LocalDateTime departureAtBeijing = LocalDateTime.of(2019, 9, 15, 13, 0, 0);
		int hours = 13;
		int minutes = 20;
		LocalDateTime arrivalAtNewYork = calculateArrivalAtNY(departureAtBeijing, hours, minutes);
		System.out.println(departureAtBeijing + " -> " + arrivalAtNewYork);
		// test:
		if (!LocalDateTime.of(2019, 10, 15, 14, 20, 0)
				.equals(calculateArrivalAtNY(LocalDateTime.of(2019, 10, 15, 13, 0, 0), 13, 20))) {
			System.err.println("测试失败!");
		} else if (!LocalDateTime.of(2019, 11, 15, 13, 20, 0)
				.equals(calculateArrivalAtNY(LocalDateTime.of(2019, 11, 15, 13, 0, 0), 13, 20))) {
			System.err.println("测试失败!");
		}
	}

	static LocalDateTime calculateArrivalAtNY(LocalDateTime bj, int h, int m) {
		// 计算到达时间
		LocalDateTime arriveBj = bj.plusHours(13).plusMinutes(20);
		// 转换为北京时间
		ZonedDateTime zbj = arriveBj.atZone(ZoneId.of("Asia/Shanghai"));
		
		// 转换为纽约时间:
        ZonedDateTime zny = zbj.withZoneSameInstant(ZoneId.of("America/New_York"));
		return zny.toLocalDateTime();
	}
}
