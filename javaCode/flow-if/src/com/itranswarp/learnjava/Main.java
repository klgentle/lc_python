package com.itranswarp.learnjava;

//import java.util.Scanner;

/**
 */
public class Main {

	public static void main(String[] args) {
		/*
		Scanner scanner = new Scanner(System.in);
		System.out.print("Height (m): ");
		double height = scanner.nextDouble();
		System.out.print("Weight (kg): ");
		double weight = scanner.nextDouble();
		// FIXME:
		double bmi = weight/(height*height);
		System.out.println(bmi);
		*/
		StringBuilder sb = new StringBuilder(1024);
		for (int i = 0; i < 1000; i++) {
		    sb.append(i);
		    if (i < 999) {
		    	sb.append(',');
		    }		    
		}
		String s = sb.toString();
		System.out.println(s);
	}

}
