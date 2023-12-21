using System;
class Program { 
    static double F(int a, int b) { return a + b; } //Вариант 1
    static double F(double a, double b) { System.Console.WriteLine("2"); return a + b; } //Вариант 2
    static double F(short a, double b) { System.Console.WriteLine("3"); return a + b; } //Вариант 3
    static double F(short a, int b) { return a + b; } //Вариант 4
    static void Main() { decimal a = 2m; System.Console.Write(F(a, 3.5)); }
}