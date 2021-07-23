package com.itranswarp.learnjava;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {
	
	public static void main(String[] args) {
	    double x = Math.abs(-123.45);
	    assert x < 0 : "x must < 0";
	    System.out.println(x);
	}

	public static void main0(String[] args) {
		//System.out.println(tax(2000, 0.1));
		//String s = null;
        //System.out.println(s);  // out:null
        //String[] s2 = new String[0];
        //System.out.println(s2.toString());
        double x = Math.abs(-123.45);
        assert x < 1;
        System.out.println(x);
        
        //System.out.println(s.toUpperCase());  //java.lang.NullPointerException
		/*
		try {
			System.out.println(tax(-200, 0.1));
		} catch (IllegalArgumentException e){
			e.printStackTrace();
		} finally {
			System.out.println("-200 end.");
		}
		try {
			System.out.println(tax(2000, -0.1));
		} catch (IllegalArgumentException e){
			e.printStackTrace();
		}finally {
			System.out.println("-0.1 end.");
		}
		*/
	}

	static double tax(int salary, double rate) {
		// TODO: 如果传入的参数为负，则抛出 IllegalArgumentException
		if (salary < 0 || rate < 0) {
			throw new IllegalArgumentException();
		}
		return salary * rate;
	}
}
