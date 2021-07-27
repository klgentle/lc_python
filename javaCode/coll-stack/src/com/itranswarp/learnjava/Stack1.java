package com.itranswarp.learnjava;

import java.util.*;

class SuffixExpression {
    int execute() {
        // TODO:
        return 0;
    }
}

/*
 * 中缀表达式，即运算符在中间，例如：1 + 2 * (9 - 5)。
 * 后缀表达式，例如：1 2 9 5 - * +。
 * 
 */
public class Stack1 {
    public static void main(String[] args) {
        String exp = "1 + 2 * (9 - 5)";
        SuffixExpression se = compile(exp);
        int result = se.execute();
        System.out.println(exp + " = " + result + " " + (result == 1 + 2 * (9 - 5) ? "✓" : "✗"));
    }

    static SuffixExpression compile(String exp) {
        // TODO:
        return new SuffixExpression();
    }
}


