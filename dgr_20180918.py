Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>>  vars()
 
  File "<pyshell#0>", line 1
    vars()
    ^
IndentationError: unexpected indent
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print __builtins__.__doc__
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> print __builtins__.abs.__doc__
abs(number) -> number

Return the absolute value of the argument.
>>> abs(10)
10
>>> abs(7)
7
>>> a = 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a = 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> a * b

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a * b
NameError: name 'b' is not defined
>>> a.__doc

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.__doc
AttributeError: 'int' object has no attribute '__doc'
>>> print a.__doc__
int(x=0) -> int or long
int(x, base=10) -> int or long

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is floating point, the conversion truncates towards zero.
If x is outside the integer range, the function returns a long instead.

If x is not a number or if base is given, then x must be a string or
Unicode object representing an integer literal in the given base.  The
literal can be preceded by '+' or '-' and be surrounded by whitespace.
The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> type(a)
<type 'int'>
>>> b = 1.5
>>> vars()
{'a': 20, 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> print b.__doc__
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
>>> type(b)
<type 'float'>
>>> c = D

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c = D
NameError: name 'D' is not defined
>>> c= "D"
>>> print c.__doc__
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
>>> type(c)
<type 'str'>
>>> burts= "E"
>>> ord(burts)
69
>>> hex(ord(burts))
'0x45'
>>> bin(ord(burts))
'0b1000101'
>>> 
