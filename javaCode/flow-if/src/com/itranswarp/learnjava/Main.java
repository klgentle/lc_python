package com.itranswarp.learnjava;

import java.util.Scanner;

/**
 * 用于计算体质指数BMI，并打印结果。
 * BMI = 体重(kg)除以身高(m)的平方
 */
public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Height (m): ");
		double height = scanner.nextDouble();
		System.out.print("Weight (kg): ");
		double weight = scanner.nextDouble();
		// FIXME:
		double bmi = weight/(height*height);
		// TODO: 用于计算体质指数BMI，并打印结果。
		System.out.println(bmi);
	}

}
