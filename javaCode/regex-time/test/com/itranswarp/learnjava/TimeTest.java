package com.itranswarp.learnjava;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class TimeTest {

	@Test
	public void testParseTime() {
		assertArrayEquals(new int[] { 0, 0, 0 }, Time.parseTime("00:00:00"));
		assertArrayEquals(new int[] { 1, 2, 3 }, Time.parseTime("01:02:03"));
		assertArrayEquals(new int[] { 10, 20, 30 }, Time.parseTime("10:20:30"));
		assertArrayEquals(new int[] { 12, 34, 56 }, Time.parseTime("12:34:56"));
		assertArrayEquals(new int[] { 23, 59, 59 }, Time.parseTime("23:59:59"));
	}

	@Test
	public void testParseTimeFailed() {
		assertThrows(IllegalArgumentException.class, () -> {
			Time.parseTime(null);
		});
		assertThrows(IllegalArgumentException.class, () -> {
			Time.parseTime("");
		});
		assertThrows(IllegalArgumentException.class, () -> {
			Time.parseTime("24:00:00");
		});
		assertThrows(IllegalArgumentException.class, () -> {
			Time.parseTime("23:60:59");
		});
		assertThrows(IllegalArgumentException.class, () -> {
			Time.parseTime("10:1:2");
		});
	}
}
