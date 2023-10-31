using System;

class Loop
{
    static void Main()
    {
        Console.Write("n = ");
        int n = int.Parse(Console.ReadLine());
        int i = 1;
        while (i <= n)
        {
            int a, b, temp;
            Console.Write("a = ");
            a = int.Parse(Console.ReadLine());
            Console.Write("b = ");
            b = int.Parse(Console.ReadLine());
            temp = a;
            Console.Write("i={0}:\tНОД({1}, {2}) = ", i, a, b);
            do
            {
                a = temp;
                if (a<b)
                {
                    temp = a;
                    a = b;
                    b = temp;
                }
                temp = a - b;
                a = b;
            }
            while (temp != b && a != 1);
            Console.WriteLine("{0}", b);
            i += 1;
        }
    }
}
