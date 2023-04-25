# скільки секунд у годині a-кількість секунд, b-кількість хвилин у годині
print("task 1")
a=60
b=60
d=a*b
print(d)
# d=seconds_per_hour
print('task 2')
seconds_per_hour=d
print(seconds_per_hour)
# кількість секунд у добі с-кільксть годин у добі
print("task 3")
c=24
f=seconds_per_hour*c
print(f)
# f=seconds_per_day
print('task 4')
seconds_per_day=f
print(seconds_per_day)
# ділення з плаваючою крапкою
print('task 5')
s=seconds_per_day/seconds_per_day
print(s)
# цілочисельне ділення
print('task 6')
x=seconds_per_day//seconds_per_day
print(x)
print('task 7')
print(3*4)
print(144/12)
print(11+1)
print(13-2)
print("task 8")
number=3
print(f"'my favorite number'{number}")
print("task 9")
name=str('mariia')
print(name.upper())
print(name.lower())
print("task 10")
poem='''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''
print(poem)
m=len(poem)
print(m)
print(poem[0:15])
q=poem.startswith("Yes")
print(q)
y=poem.endswith("I shall live!")
print(y)
r=poem.find(",")
print(r)
z=poem.rfind(",")
print(z)
h=poem.count(",")
print(h)
e=poem.isalnum()
print(e)