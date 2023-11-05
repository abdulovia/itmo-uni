using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите коэффициенты уравнения: ");
        Console.Write("a = ");
        int a = int.Parse(Console.ReadLine());
        Console.Write("b = ");
        int b = int.Parse(Console.ReadLine());
        Console.Write("c = ");
        int c = int.Parse(Console.ReadLine());

        double x1, x2;
        int res = Roots.EqRoots(a, b, c, out x1, out x2);
        if (res == 1)
            Console.WriteLine("Корни уравнения с коэффициентами a = " + a + ", b = " + b + ", c = " + c + " равны x1 = " + x1 + ", x2 = " + x2);
        else if (res == 0)
            Console.WriteLine("Корень уравнения с коэффициентами a = " + a + ", b = " + b + ", c = " + c + " один x1 = x2 = " + x1);
        else
            Console.WriteLine("Корней уравнения с коэффициентами a = " + a + ", b = " + b + ", c = " + c + " нет.");
    }
}
