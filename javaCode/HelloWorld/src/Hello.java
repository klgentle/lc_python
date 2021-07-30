/**
 * @author pactera
 *
 */
import java.util.*;
import java.math.*;
import java.time.LocalDate;

public class Hello {
	public static void main(String[] args) {
		System.out.println(System.currentTimeMillis());
		
	}
	
    public static void main6(String[] args) {
        Random r = new Random(12345);  // 伪随机数
        for (int i = 0; i < 10; i++) { 
            System.out.println(r.nextInt(100));  
        }
        // 51, 80, 41, 28, 55...
    }

	public static void main5(String[] args)
	{
        // 5λͬѧ�ĳɼ�:
        int[] ns = new int[5];
        ns[0] = 68;
        ns[1] = 79;
        ns[2] = 91;
        ns[3] = 85;
        ns[4] = 62;
        System.out.println(Arrays.toString(ns));
	}

    public static void main3(String[] args)
    {
        int[] a = {1,2,3,6,8,9};
        for (int elem : a)
        	System.out.printf("%d ",elem);
        System.out.println();
//        System.out.println(Arrays.toString(a));
        BigDecimal b1 = new BigDecimal(1.0/10);
        System.out.println(b1);
        BigDecimal b2 = new BigDecimal(1 - 9.0 / 10);
        System.out.println(b2);
        System.out.println(b1.subtract(b2));
        System.out.println(LocalDate.now());
        
        String s = """
                SELECT * FROM
                  users
                WHERE id > 100
                ORDER BY name DESC
                """;
        System.out.println(s);
    }

	
	public static void main0(String[] args) {
		
        double x = 1.0 / 10;
        double y = 1 - 9.0 / 10;
        System.out.println(x);
        System.out.println(y);
        System.out.println("x is equal to y? " +isEqual(x,y));
        int n2 = 5;
        double d = 1.2 + 24.0 / n2; // 6.0
        System.out.println(d);
        
        int n3= (int) (2.6 + 0.5);
        int n4= (int) (2.4 + 0.5); 
        System.out.println(n3);
        System.out.println(n4);
	}
	
	public static boolean isEqual(double x, double y)
	{
        double r = Math.abs(x-y);
        if (r<0.0001)
        	return true;
        else
        	return false;
	}
    public static void main1(String[] args) {
        double a = 1.0;
        double b = 3.0;
        double c = -4.0;
        // System.out.println(Math.sqrt(2)); ==> 1.414
        // TODO:
        double d = Math.sqrt(b*b-4*a*c);
        double r1 = (-b + d)/(2*a);
        double r2 = (-b - d)/(2*a);
        
        System.out.println(r1);
        System.out.println(r2);
        System.out.println(r1 == 1 && r2 == -4 ? "OK" : "not");
    }
    
	public static void main2(String[] args) {
//		 TODO Auto-generated method stub
		System.out.println("Hello, World!");
		int n = 100;
		System.out.println("n = " + n);
		int i3 = 2_000_000_000; 
		System.out.printf("i3 = %d\n", i3); 
		boolean b1 = true;
		System.out.println("b1 = " + b1);
	}
	
	
}
