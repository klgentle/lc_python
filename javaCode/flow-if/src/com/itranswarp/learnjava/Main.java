package com.itranswarp.learnjava;

import java.util.Scanner;

/**
 * ���ڼ�������ָ��BMI������ӡ�����
 * BMI = ����(kg)�������(m)��ƽ��
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
		// TODO: ���ڼ�������ָ��BMI������ӡ�����
		System.out.println(bmi);
	}

}
