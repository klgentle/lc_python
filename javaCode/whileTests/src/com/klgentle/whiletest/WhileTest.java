package com.klgentle.whiletest;

public class WhileTest {

	public static void main0(String[] args) {
		// TODO Auto-generated method stub
		int sum = 0;
		int m = 20;
		int n = 100;
		int i = m;
		while (i <= n) {
			sum = sum + i;
			i = i+1;
		}
		System.out.println(sum);
	}

    public static void main1(String[] args) {
        double pi = 0;
        double sum = 1.0;
        int sign = -1;
        for (int i=3; i < 10000; i=i+2) {
            sum = sum + sign *1.0/i;
            //System.out.println(sum);
            sign = sign * (-1);
        }
        pi = 4.0*sum;
        System.out.println(pi);
    }
    
    public static void main2(String[] args) {
        int[][] scores = {
                { 82, 90, 91 },
                { 68, 72, 64 },
                { 95, 91, 89 },
                { 67, 52, 60 },
                { 79, 81, 85 },
        };
        // TODO:
        double sum = 0.0;
        int count = 0;
        for (int[] arr : scores) {
            for (int n : arr) {
                 sum = sum + n;
                 count ++;
            }
        }    

        double average = sum/count;
        System.out.println(average);
    	
    }
    
    public static void main(String[] args) {
        Person ming = new Person();
        ming.setName("С��");
        ming.setAge(12);
        System.out.println(ming.getAge());
    }

}

class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }

}
