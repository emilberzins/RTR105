Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
>>> str2 = "there"
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> str3 = "123"
>>> str3= str3 +1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3= str3 +1
TypeError: must be str, not int
>>> x= int(srt3) +1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x= int(srt3) +1
NameError: name 'srt3' is not defined
>>> x = int(str3) + 1
>>> print(x)
124
>>> name = input("Enter:")
Enter:Chuck
>>> print(name)
Chuck
>>> apple=input("Enter:")
Enter:100
>>> x = apple - 10
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = apple - 10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(apple) - 10
>>> print(x)
90
>>> fruit = "banana"
>>> letter = fruit[1]
>>> print(letter)
a
>>> x=3
>>> w = fruit[x-1]
>>> print(w)
n
>>> fruit = "banana"
>>> print(len(fruit))
6
>>> fruit= "banana"
>>> word = "banana"
>>> count = 0
>>> greet = "Hello Bob"
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print("hi there".lower())
hi there
>>> stuff = "hello world"
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
