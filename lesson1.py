 >>> c=a+b
>>> print (c)
6.5
>>> type(a)
<class 'int'>
>>> type(c)
<class 'float'>
>>> v= input('Введите число от 1 до 10: ')
Введите число от 1 до 10:
>>> v
''
>>> print (v)

>>> v= input('Введите число от 1 до 10: ')
Введите число от 1 до 10: 7
>>> print (input*10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'builtin_function_or_method' and '
int'
>>> print (v+100
...
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> print (v+10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> print(int(v)+10)
17
>>> type(v)
<class 'str'>
>>> name = input ('Введите ваше имя: ')
Введите ваше имя: Павел
>>> print ('Привет,'+ name+'!'+'Как дела?')
Привет,Павел!Как дела?
>>> print ('Привет,'+ ' ' name+'!'+'Как дела?')
  File "<stdin>", line 1
    print ('Привет,'+ ' ' name+'!'+'Как дела?')
                             ^
SyntaxError: invalid syntax
>>> print ('Привет,'+ ' '+ name+'!'+ ' '+'Как дела?')
Привет, Павел! Как дела?
>>> float('1')
1.0
>>> int('2.5')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2.5'
>>> bool(1)
True
>>> bool('')
False
>>> bool(0)
False
>>> bool(2.5)
True
>>> int(7.7)
7
>>> a=list ()
>>> b=[]
>>> c=[1,'Вася'false]
  File "<stdin>", line 1
    c=[1,'Вася'false]
                   ^
SyntaxError: invalid syntax
>>> c=[1,'Вася',false]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> c=[1,'Вася',False]
>>> len(c)
3
>>> c.append(500)
>>> c
[1, 'Вася', False, 500]
>>> c(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> c[1]
'Вася'
>>> c.append(500,400)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)
>>> c[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> c[1:2]
['Вася']
>>> c[1:3]
['Вася', False]
>>> c[:3)
  File "<stdin>", line 1
    c[:3)
        ^
SyntaxError: invalid syntax
>>> c[:3]
[1, 'Вася', False]
>>> c[-2]
False
>>> c
[1, 'Вася', False, 500]
>>> c[-2:]
[False, 500]
>>> x=c[3]
>>> type (x)
<class 'int'>
>>> x*5
2500
>>> c.count ("Вася")
1
>>> c.count(1)
1
>>> c.count('1')
0
>>> c.index(500)
3
>>> c.sort
<built-in method sort of list object at 0x0000000001A51A88>
>>> c.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() < int()
>>> list = [2,3,4,5,6,7]
>>> len(list)
6
>>> del list[3]
>>> list
[2, 3, 4, 6, 7]
>>> list.remove(6)
>>> list
[2, 3, 4, 7]
>>> newlist = [2,3,4,5,6,7]
>>> newlist.append('python')
>>> newlist
[2, 3, 4, 5, 6, 7, 'python']
>>> newlist[0;2;-1]
  File "<stdin>", line 1
    newlist[0;2;-1]
             ^
SyntaxError: invalid syntax
>>> newlist[0:2:-1]
[]
>>> newlist[1]
3
>>> newlist[0,2,-1)
  File "<stdin>", line 1
    newlist[0,2,-1)
                  ^
SyntaxError: invalid syntax
>>> newlist
[2, 3, 4, 5, 6, 7, 'python']
>>> print(newlist[0],newlist[2], newlist[-1])
2 4 python
>>> newlist [:-2)
  File "<stdin>", line 1
    newlist [:-2)
                ^
SyntaxError: invalid syntax
>>> newlist [:-2]
[2, 3, 4, 5, 6]
>>> newlist [1:2]
[3]
>>> del newlist[2]
>>> newlist
[2, 3, 5, 6, 7, 'python']
>>> newlist[1:4]
[3, 5, 6]
>>> len(newlist)
6
>>> newlist+1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
>>> x= dict()
>>> user = {"name": "Маша", "age": 25, "job": "Python developer", "have_airplain
": False}
>>> user
{'have_airplain': False, 'name': 'Маша', 'job': 'Python developer', 'age': 25}
>>> len(user)
4
>>> print(user['name'])
Маша
>>> print(user['job'])
Python developer
>>> user [gender]= 'f'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'gender' is not defined
>>> del user ["city"]'
  File "<stdin>", line 1
    del user ["city"]'
                     ^
SyntaxError: EOL while scanning string literal
>>> del user ["city"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'city'
>>> user ["city"]="Moscow"
>>> user
{'have_airplain': False, 'name': 'Маша', 'city': 'Moscow', 'job': 'Python develo
per', 'age': 25}
>>> del user ["city"])
  File "<stdin>", line 1
    del user ["city"])
                     ^
SyntaxError: invalid syntax
>>> del user ["city"]
>>> user
{'have_airplain': False, 'name': 'Маша', 'job': 'Python developer', 'age': 25}
>>> user.get("job")
'Python developer'
>>> user.keys()
dict_keys(['have_airplain', 'name', 'job', 'age'])
>>> weather = {"city": "Moscow","temp": "+25", "wind":"north-east"}
>>> weather
{'temp': '+25', 'wind': 'north-east', 'city': 'Moscow'}
>>> weather {city}
  File "<stdin>", line 1
    weather {city}
            ^
SyntaxError: invalid syntax
>>> weather ["city"]
'Moscow'
>>> weather["temp"]=
  File "<stdin>", line 1
    weather["temp"]=
                   ^
SyntaxError: invalid syntax
>>> weather["temp"]="+10"
>>> weather
{'temp': '+10', 'wind': 'north-east', 'city': 'Moscow'}
>>> len(weather)
3
>>> weather.keys("city")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: keys() takes no arguments (1 given)
>>> weather.keys()
dict_keys(['temp', 'wind', 'city'])
>>> dict+keys
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'keys' is not defined
>>> dict_keys
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dict_keys' is not defined
>>> city in wether.keys()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'city' is not defined
>>> city in weather.keys
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'city' is not defined
>>> "city" in weather
True
>>> "city" in weather.keys()
True
>>> 'city' in weather
True
>>> ^Z


c:\Projects\lesson1>test.py
"test.py" не является внутренней или внешней
командой, исполняемой программой или пакетным файлом.

c:\Projects\lesson1> echo >test.py

c:\Projects\lesson1>test.py
  File "C:\Projects\lesson1\test.py", line 1
SyntaxError: Non-UTF-8 code starting with '\x90' in file C:\Projects\lesson1\tes
t.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-026
3/ for details

c:\Projects\lesson1> python test.py
  File "test.py", line 1
SyntaxError: Non-UTF-8 code starting with '\x90' in file test.py on line 1, but
no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

c:\Projects\lesson1>  test.py

c:\Projects\lesson1>python tet.py
python: can't open file 'tet.py': [Errno 2] No such file or directory

c:\Projects\lesson1>python test.py

c:\Projects\lesson1> python test.py

c:\Projects\lesson1>python test.py
5

c:\Projects\lesson1>