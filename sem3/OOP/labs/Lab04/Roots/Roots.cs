using System;

class Roots
{
    public static int EqRoots (int a, int b, int c, out double x1, out double x2) 
    {
        int D = b*b - 4*a*c;
        if (D > 0)
        {
            x1 = (-b + Math.Sqrt(D)) / (2 * a);
            x2 = (-b - Math.Sqrt(D)) / (2 * a);
            return 1;
        }
        else if (D == 0)
        {
            x1 = -b / (2 * a);
            x2 = x1;
            return 0;
        }
        else
        {
            x1 = 0;
            x2 = 0;
            return -1;
        }
    }
}