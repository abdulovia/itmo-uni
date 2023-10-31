using System;

class Strelba
{
    static void Main()
    {
        Console.Write("Количество выстрелов = ");
        int n = int.Parse(Console.ReadLine());
        int res = 0;
        double x, y;
        Random rnd = new Random();
        // центр мишени случайным образом
        double x0 = rnd.Next(3), y0 = rnd.Next(3);
        Console.WriteLine("({0}, {1}) – центр мишени", x0, y0);
        for (int i = 1; i <= n; i++)
        {
            Console.Write("x = ");
            x = double.Parse(Console.ReadLine());
            Console.Write("y = ");
            y = double.Parse(Console.ReadLine());
            // случайная помеха выстрелу
            double x1 = rnd.NextDouble(), y1 = rnd.NextDouble();
            Console.WriteLine("({0}, {1}) – помеха выстрелу", x1, y1);
            // результат выстрела
            int shot_res = 0;
            // variant 1
            if (i % 2 == 1)
            {
                x = x + x1 - x0;
                y = y + y1 - y0;
                if (x * x + y * y <= 1)
                    shot_res += 10;
                else if (x * x + y * y <= 4)
                    shot_res += 5;
            }
            // variant 2
            else
            {
                x = x + x1 - x0;
                y = y + y1 - y0;
                if (x * x + y * y <= 1)
                    shot_res += 10;
                else if (x * x + y * y <= 4)
                    shot_res += 5;
                else if (x * x + y * y <= 9)
                    shot_res += 1;
            }
            Console.WriteLine("Результат {0} выстрела {1} очков", i, shot_res);
            res += shot_res;
        }
        Console.WriteLine("Сумма очков = {0}. Поздравляем!", res);
    }
}