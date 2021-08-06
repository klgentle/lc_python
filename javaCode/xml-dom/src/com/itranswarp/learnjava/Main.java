package com.itranswarp.learnjava;

import java.io.InputStream;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Node;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) throws Exception {
		InputStream input = Main.class.getResourceAsStream("/book.xml");
		// 解析并获取Document对象:
		DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
		DocumentBuilder db = dbf.newDocumentBuilder();
		Document doc = db.parse(input);
		printNode(doc, 0);
	}

	static void printNode(Node n, int indent) {
		for (int i = 0; i < indent; i++) {
			System.out.print(' ');
		}
		switch (n.getNodeType()) {
		case Node.DOCUMENT_NODE:
			System.out.println("Document: " + n.getNodeName());
			break;
		case Node.ELEMENT_NODE:
			System.out.println("Element: " + n.getNodeName());
			break;
		case Node.TEXT_NODE:
			if (n.getNodeValue() != null) { 
				System.out.println("Text: " + n.getNodeName() + " = [" + n.getNodeValue() +"]");
			}
			break;
		case Node.ATTRIBUTE_NODE:
			System.out.println("Attr: " + n.getNodeName() + " = " + n.getNodeValue());
			break;
		case Node.CDATA_SECTION_NODE:
			System.out.println("CDATA: " + n.getNodeName() + " = " + n.getNodeValue());
			break;
		case Node.COMMENT_NODE:
			System.out.println("Comment: " + n.getNodeName() + " = " + n.getNodeValue());
			break;
		default:
			System.out.println("NodeType: " + n.getNodeType() + ", NodeName: " + n.getNodeName());
		}
		for (Node child = n.getFirstChild(); child != null; child = child.getNextSibling()) {
			printNode(child, indent + 1);
		}
	}
}
