# Урок 1. Создание простейших программ на Python
1. Создайте программу для запроса имени пользователя.
	- В режиме интерпретатора, запросите имя и фамилию у пользователя, сохраните их в виде переменных и выведите на экран в формате ‘Привет, Имя Фамилия!’;
	- Сохраните эту программу в виде файла ‘Hello.py’, добейтесь ее выполнения в режиме командной строки.
2. Напишите программу, позволяющему пересчитать температуру в градусах Фаренгейта в температуру в градусах Цельсия. На экране отображается и градусы Фаренгейта и градусы Цельсия.
	- Расчет температуры происходит через статическую величину, указанную в программе. Программа пересчитывает Формула для расчета: TC = (TF – 32) / 1.8 где TC – градусы Цельсия, TF – градусы Фаренгейта;
	- Пользователь вводит градусы Фаренгейта с клавиатуры.
3. Составьте программу для расчета площади треугольника по формуле Герона. Используйте модуль math и функцию sqrt() Формула для расчета: S = sqrt(p(p -a)(p-b)(p-c)), где р – полупериметр
	- Расчет формулы можно проводить только, если треугольник существует;
	- Включите в программу вариант произвольного и равностороннего треугольника.
4. Создайте программу для реализации «черепашьей графики». Используйте модуль turtle.
	- Заставьте Вашу черепаху пройти замкнутый многоугольный контур (с числом углов больше четырех), вернувшись в начальную точку;
	- Отправьте черепашку по пути: 
	
	![image](https://user-images.githubusercontent.com/112972833/209082785-c82012db-b0f2-485f-9f07-ef426926444e.png)
	
5. Создайте программу для перевода числа, введенного пользователем с клавиатуры, в формат дни:часы:минуты:секунды