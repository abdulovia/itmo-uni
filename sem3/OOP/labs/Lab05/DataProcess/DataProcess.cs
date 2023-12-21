using System;

class DataProcess
{
    private static int Sum(int[] a)
    {
        int s = 0;
        for (int i = 0; i < a.GetLength(0); i++)
            s += a[i];
        return s;
    }
    private static double Avg(int[] a, int s)
    {
        return (double)s / a.GetLength(0);
    }
    private static int NegativeSum(int[] a)
    {
        int s = 0;
        for (int i = 0; i < a.GetLength(0); i++)
            if (a[i] < 0)
                s += a[i];
        return s;
    }
    private static int IndexSum(int[] a)
    {
        int s = 0;
        // Сумма элементов с четными индексами
        for (int i = 0; i < a.GetLength(0); i+=2)
            s += a[i];
        return s;
    }
    static void Main()
    {
        int[] a = new int[4];
        for (int ix = 0; ix < a.GetLength(0); ix++)
        {
            Console.Write("Enter value for [{0}] : ", ix);
            string val = System.Console.ReadLine();
            a[ix] = int.Parse(val);
        }
        Console.WriteLine();
        int s = Sum(a);
        Console.WriteLine("Сумма: {0}", s);
        double avg = Avg(a, s);
        Console.WriteLine("Среднее значение: {0}", avg);
        int negs = NegativeSum(a);
        Console.WriteLine("Сумма отрицательных: {0}", negs);
        int isum = IndexSum(a);
        Console.WriteLine("Сумма с четными i: {0}", isum);
    }
}
