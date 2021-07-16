class Tests{
    public static void main(String[] args)
    {
        int p = 1200, q = 8;
        //System.out.println(gcd(p, q));

        //声明初始化
        double[] a2 = {1, 1, 2, 3, 5, 8, 9, 10, 11,12,14,88, 99};

        Tests test = new Tests(); //实例化对象，再调用方法
        //System.out.println(test.getMax(a2));
        
        double[] a3 = reverse(a2);
        for(int i= 0; i < a3.length; i++)
            System.out.println(a3[i]);
    }

    public static int gcd(int p, int q)
    {
        if (q == 0) return p;
        int r = p % q;
        return gcd(q, r);
    }

    public void init()
    {
        int N = 20;
        double[] a1 = new double[N];
    }

    public double getMax(double[] a)
    {
        double max = a[0];
        for (int i = 1; i < a.length; i++)
            if (a[i] > max) max = a[i];

        return max;
    }

    public static double[] reverse(double[] a)
    {
        int N = a.length;
        for (int i = 0; i <N/2; i++)
        {
            double temp = a[i];
            a[i] = a[N-1-i];
            a[N-1-i] = temp;
        }
        return a;
    }
}
