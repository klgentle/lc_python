package com.itranswarp.learnjava;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;

class TemplateTest {

	@Test
	public void testIsValidTel() {
		Template t = new Template("Hello, ${name}! You are learning ${lang}!");
		Map<String, Object> data = new HashMap<>();
		data.put("name", "Bob");
		data.put("lang", "Java");
		System.out.println(t.render(data));
		assertEquals("Hello, Bob! You are learning Java!", t.render(data));
	}
}
