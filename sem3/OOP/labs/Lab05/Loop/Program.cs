using System;

class Loop
{
    static void Main()
    {
        int[] MyArray;
        int n = int.Parse(Console.ReadLine());
        MyArray = new int[n];
        for (int i = 0; i < MyArray.Length; ++i)
        {
            Console.Write("a[{0}]=",i);
            MyArray[i] = int.Parse(Console.ReadLine());
        }
        foreach (int x in MyArray) Console.Write("{0} ", x);
        Console.WriteLine();
        int j = 0;
        while (j != MyArray.Length)
        {
            if (MyArray[j] % 2 == 0) MyArray[j] = 0;
            Console.Write("{0} ", MyArray[j]);
            j++;
        }
    }
}
