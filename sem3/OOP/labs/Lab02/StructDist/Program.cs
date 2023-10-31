using System;

public struct Distance
{
    public int foot;
    public int inch;
}

class Program
{
    static void Main()
    {
        Distance X;
        Console.WriteLine("Enter the first distance length: ");
        X.inch = int.Parse(Console.ReadLine());
        Distance Y;
        Console.WriteLine("Enter the second distance length: ");
        Y.inch = int.Parse(Console.ReadLine());
        Distance Z;
        Z.inch = X.inch + Y.inch;
        X.foot = (int)(X.inch / 12);
        X.inch = X.inch % 12;
        Console.WriteLine("First distance = {0}\' - {1}\"", X.foot, X.inch);
        Y.foot = (int)(Y.inch / 12);
        Y.inch = Y.inch % 12;
        Console.WriteLine("Second distance = {0}\' - {1}\"", Y.foot, Y.inch);
        Z.foot = (int)(Z.inch / 12);
        Z.inch = Z.inch % 12;
        Console.WriteLine("Sum of distances = {0}\' - {1}\"", Z.foot, Z.inch);
    }
}