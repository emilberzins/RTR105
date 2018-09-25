Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> input("cienijamais lietotaj, ludzu, ievadi vienu skaitli: ")
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("cienijamais lietotaj, ludzu, ievadi vienu skaitli: ")
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("cienijamais lietotaj, ludzu, ievadi vienu skaitli: ")
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 21
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 21, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 6
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 6, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 6
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 6, '__package__': None, 'x': 36, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 2222
mans_mainigais = 2222
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 2222, '__package__': None, 'x': 4937284, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 2
mans_mainigais =      2.000
vai tu esi ievadijis skaitli:=     2.0000
vel atmina tagat ir ari mainigais x =       4.0000000
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 2, '__package__': None, 'x': 4, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
cienijamais lietotaj, ludzu, ievadi vienu skaitli: s

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
