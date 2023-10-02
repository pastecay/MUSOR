#1
a = int(input())
print(a)
print(a + 1)
print(a + 2)
#2
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
#3
x = int(input())
print('Объем =', x * x * x)
print('Площадь полной поверхности =', 6 * x * x)
#4
a = int(input())
b = int(input())
print(3 * (a+b) * (a+b) * (a+b) + 275 * b * b - 127 * a - 41)
#5
score = int(input())
print('Следующее за числом', score, 'число:', score  + 1)
print('Для числа', score, 'предыдущее число:', score - 1)
#6
x = int(input())
y = int(input())
z = int(input())
c = int(input())
print(3 * (x + y + z + c))
#7
a = int(input())
b = int(input())
c = int(input())
x = a + b * (c - 1)
print(x)
#8
x = int(input())
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')
#9
a = int(input())
b = int(input())
print(b // a)
print(b % a)
#10
n = int(input())
print(n//2 + n%2)
#11
m = int(input())
h = m // 60
s = m % 60
print(m, "мин - это", h, "час", s, "минут.")
#12
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", c + b + a)
print("Произведение цифр =", c * b * a)
#13
number_of_penguins = input()
print('   _~_    ' * int(number_of_penguins))
print('  (o o)   ' * int(number_of_penguins))
print(' /  V  \\  ' * int(number_of_penguins))
print('/(  _  )\\ ' * int(number_of_penguins))
print('  ^^ ^^   ' * int(number_of_penguins))
#14
abc = int(input())
k = 1
n = (abc // 10 ** k) % 10
print(n)
#15
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)
#16
n = int(input())
print(1 - n)
#17
n = int(input())
print((n//2+1)*2)
#18
v = int(input())
t = int(input())
a = v * t
n = a // 109
print(-(109 * n - a))
#19
h = float(input())
a = float(input())
b = float(input())
print(int(1 + (h - b - 1) / (a - b)))
#20
