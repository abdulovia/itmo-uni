using System;

class Program
{
    static void Main()
    {
        Console.Write("Треугольник равносторонний (y/n): ");
        string s = Console.ReadLine();
        if (s == "y")
        {
            Console.Write("Введите сторону равностороннего треугольнкиа: ");
            int a = int.Parse(Console.ReadLine());
            double ans = Operation.Area(a);
            Console.WriteLine("Площадь равностороннего треугольника: " + ans);
        }
        else if (s == "n")
        {
            Console.Write("Введите первую сторону: ");
            int a = int.Parse(Console.ReadLine());
            Console.Write("Введите вторую сторону: ");
            int b = int.Parse(Console.ReadLine());
            Console.Write("Введите третью сторону: ");
            int c = int.Parse(Console.ReadLine());
            double ans = Operation.Area(a, b, c);
            if (ans == 0.0)
            {
                Console.WriteLine("Triangle doesn't exist");
            }
            else
            {
                Console.WriteLine("Площадь треугольника: " + ans);
            }
        }
    }
}