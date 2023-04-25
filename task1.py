print('task1')
age=input("What is your name?")
print("Nice "+ age)
print('task2')
welcome=input('Say hello:')
print('Hello, Sasha, wold you like to learn some Python today?')
print('task3')
famous_person='Helen Keller'
message= input('My favorit quote:')
print(famous_person + ''' There are no shortcuts to any place worth going''')
print('task4')
name: str="\n\tHuivaniuk \n\tMariia"
print(name)
x=name.strip()
print( "of all",x, "is my favorite")
p=name.lstrip()
print(p)
e=name.rstrip()
print(e)
print('task5')
name1="Huivaniuk Mariia"
print(name1+''' address Cheska respublika,\n Praha,\n ZIP code: 14400 ''')
print('task6')
m=1
i=0.0254
f=0.3048
c=1609.344
co=0.9148
print('{0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f}'.format(m, i, f, c, c ))
# 1 дні канікул
print('task7')
setup = 'Vacation lasted 2 days'
setup.ljust(10)
print(setup.ljust(10))
seconds_per_hour=60*60
seconds_per_day=seconds_per_hour*48
print(seconds_per_hour )
print(seconds_per_day)
print('task8')
c=10
F=32+9/5*c
K=c+273.15
print(F)
print(K)
print('{2:15f} {0:15f} {1:15f}'.format(K, c, F))
print('task9')
a=6
b=2
c=5
h=9
print(f'6+2+5+9={a+b+c+h}')
#print('task10')
#x1=39.9075000
#y1=116.3972300
#x2=50.4546600
#y2=30.5238000
#import math
#a=math.radians(x1, y1, x2, y2)
#print(arccos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2)))
print('task9.1')
n = int(input('enter a number'))
c=n%10
n = n // 10
b=n %10
a =n// 10
h = a % 10
t = n // 100
print(c+b+h+t)





