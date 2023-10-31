using System;

class TriArea
{
    static void Main()
    {
        try
        {
        Console.WriteLine("Please enter the perimeter");
        string temp = Console.ReadLine( );
        int P = Int32.Parse(temp);
        
        int a = P / 3;
        double p = P / 2;
        double S = Math.Sqrt(p*(p-a)*(p-a)*(p-a));

        Console.WriteLine("Сторона\tПлощадь");
        Console.WriteLine("{0}\t{1:f2}", a, S);
        }
        catch (FormatException e)
        {
            Console.WriteLine("A format exception was thrown: {0}", e.Message);
        }
        catch(Exception e)
        {
            Console.WriteLine("An exception was thrown: {0}", e.Message);
        }
        
    }
}
