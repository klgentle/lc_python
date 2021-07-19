package com.itranswarp.sample;

import javax.xml.XMLConstants;

public class Main {

	public static void main(String[] args) {
		Greeting g = new Greeting();
		System.out.println(g.hello(XMLConstants.XML_NS_PREFIX));
	}

}
