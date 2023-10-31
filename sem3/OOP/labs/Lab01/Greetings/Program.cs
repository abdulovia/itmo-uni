using System;

class Greeter
{
    static void Main()
    {
        string myName;
        Console.WriteLine("Please enter you name");
        myName = Console.ReadLine();
        Console.WriteLine("Hello, {0}", myName);
    }
}