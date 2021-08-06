package com.itranswarp.learnjava;

import java.io.InputStream;

import com.fasterxml.jackson.dataformat.xml.JacksonXmlModule;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

public class Main {
	public static void main(String[] args) throws Exception {
		InputStream input = Main.class.getResourceAsStream("/book.xml");
		JacksonXmlModule module = new JacksonXmlModule();
		XmlMapper mapper = new XmlMapper(module);
		Book book = mapper.readValue(input, Book.class);
		System.out.println(book.id);
		System.out.println(book.name);
		System.out.println(book.author);
		System.out.println(book.isbn);
		System.out.println(book.tags);
		System.out.println(book.pubDate);
		System.out.println(book.lang);  // null
	}
}
