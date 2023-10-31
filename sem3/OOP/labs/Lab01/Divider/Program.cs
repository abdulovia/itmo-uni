using System;

class DivideIt
{
    static void Main()
    {
        try
        {
        Console.WriteLine("Please eneter the first integer");
        string temp = Console.ReadLine( );
        int i = Int32.Parse(temp);
        Console.WriteLine("Please eneter the second integer");
        temp = Console.ReadLine( );
        int j = Int32.Parse(temp);

        int k = i / j;
        Console.WriteLine("k = {0}", k);
        }
        catch (FormatException e){
            Console.WriteLine("A format exception was thrown: {0}", e.Message);
        }
        catch(Exception e)
        {
            Console.WriteLine("An exception was thrown: {0}", e.Message);
        }
    }
}
