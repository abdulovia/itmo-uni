using System;

class Sum_Limits
{
    static void Main()
    {
        Console.Write("k = ");
        int k = int.Parse(Console.ReadLine());
        Console.Write("m = ");
        int m = int.Parse(Console.ReadLine());
        long s = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (i > k && i < m) continue;
            s += i;
        }
        Console.WriteLine("Сумма = {0}", s);
    }
}