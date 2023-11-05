using System;

class Operation
{
    public static double Area (int a, int b, int c)
    {
        bool ok = Exists(a, b, c);
        if (ok)
        {
            double p = (a + b + c) / 2;
            return Math.Sqrt(p*(p-a)*(p-b)*(p-c));
        }
        else
        {
            return 0;
        }
    }
    private static bool Exists (int a, int b, int c)
    {
        if (a + b > c && a + c > b && b + c > a)
            return true;
        else
            return false;
    }
    public static double Area (int a)
    {
        double p = a * 3 / 2;
        return Math.Sqrt(p*(p-a)*(p-a)*(p-a));
    }
}