using System;

class Visokosniy_Year
{
    static void Main()
    {
        try
        {
            Console.Write("year = ");
            int year = int.Parse(Console.ReadLine());
            if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
                Console.WriteLine("{0} – високосный год", year);
            else Console.WriteLine("Не високосный год");
        }
        catch (Exception e)
        {
            Console.WriteLine("Введено некорректное значение");
        }
    }
}
