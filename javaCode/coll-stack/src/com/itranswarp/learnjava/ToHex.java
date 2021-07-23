package com.itranswarp.learnjava;

import java.util.*;

public class ToHex {
    public static void main(String[] args) {
        String hex = toHex(12500);
//        System.out.println("out:" + hex);
        if (hex.equalsIgnoreCase("30D4")) {
            System.out.println("测试通过");
        } else {
            System.out.println("测试失败");
        }
    }

    static String toHex(int n) {
    	Map<Integer, String> map = new HashMap<> ();
    	for (int i = 0; i <= 9; i++) {
    		map.put(i, String.valueOf(i));
    	}
    	map.put(10, "A");
    	map.put(11, "B");
    	map.put(12, "C");
    	map.put(13, "D");
    	map.put(14, "E");
    	map.put(15, "F");
    	Deque<String> stack = new LinkedList<>();
    	while (n != 0) {
    		Integer mod = n % 16;
//    		System.out.println(mod);
    		stack.addFirst(map.get(mod));
    		n = n / 16;
    	}
    	// TODO Deque to String
    	StringBuilder sb = new StringBuilder(1024);
    	while (stack.peekFirst() != null) {
    	    sb.append(stack.removeFirst());
    	}
        return sb.toString();
    }
}

