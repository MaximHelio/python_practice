Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(a)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=int(a)
NameError: name 'a' is not defined
>>> a=int(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=int(a)
NameError: name 'a' is not defined
>>> a = int(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a = int(a)
NameError: name 'a' is not defined
>>> a=input('숫자를 하나 입력해 보세요:')
숫자를 하나 입력해 보세요:23
>>> a
'23'
>>> type(a)
<class 'str'>
>>> a= int(a)
>>> type(a)
<class 'int'>
>>> a = float(a)
>>> type(a)
<class 'float'>
>>> c=17/7
>>> 
>>> c
2.4285714285714284
>>> type(c)
<class 'float'>
>>> c=round(c,1)
>>> c
2.4
>>> def separate():
	a=int(input('자연수 중 하나를 입력하세요:'))
	if a % 2 == 0:
		print('짝수')
	else:
		print('홀수')

		
>>> separate()
자연수 중 하나를 입력하세요:2
짝수
>>> 1
1
>>> separate(1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    separate(1)
TypeError: separate() takes 0 positional arguments but 1 was given
>>> separate()
자연수 중 하나를 입력하세요:1
홀수
>>> def separate()
SyntaxError: invalid syntax
>>> def separate():
	a=int(input('자연수 중 하나를 입력하세요:'))
	if a % 2 == 0:
		print('짝수')
	else: print('홀수')

	
>>> separate()
자연수 중 하나를 입력하세요:54
짝수
>>> separate()
자연수 중 하나를 입력하세요:37
홀수
>>> price=[23, 40, 67]
>>> for i in price:
	i*1.1

	
25.3
44.0
73.7
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded =input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result= service*1.1
	else:
		result=service

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    service_price()
  File "<pyshell#55>", line 5, in service_price
    result= service*1.1
TypeError: can't multiply sequence by non-int of type 'float'
>>> price=[23, 34, 67]
>>> a,b,c=price
>>> a
23
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=service*1.1
	else:
		result=service

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:A
부가세를 포함합니까? y/n:Y
>>> 
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    service_price()
  File "<pyshell#68>", line 5, in service_price
    result=service*1.1
TypeError: can't multiply sequence by non-int of type 'float'
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=price*1.1
	else:
		result=price

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    service_price()
  File "<pyshell#74>", line 5, in service_price
    result=price*1.1
TypeError: can't multiply sequence by non-int of type 'float'
>>> type(a)
<class 'int'>
>>> int(price)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(price)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> type(price)
<class 'list'>
>>> def service_price():
	service=int(input('서비스 종류를 입력하세요, a/b/c:'))
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=price*1.1
	else:
		result=price

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    service_price()
  File "<pyshell#80>", line 2, in service_price
    service=int(input('서비스 종류를 입력하세요, a/b/c:'))
ValueError: invalid literal for int() with base 10: 'a'
>>> price=23, 40, 67
>>> a,b,c=price
>>> a
23
>>> type(price)
<class 'tuple'>
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=price*1.1
	else:
		result=price

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    service_price()
  File "<pyshell#87>", line 5, in service_price
    result=price*1.1
TypeError: can't multiply sequence by non-int of type 'float'
>>> tuple(price)
(23, 40, 67)
>>> price
(23, 40, 67)
>>> list(price)
[23, 40, 67]
>>> tuple(price)
(23, 40, 67)
>>> a
23
>>> b
40
>>> a=23
>>> b=40
>>> c=67
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> price
(23, 40, 67)
>>> service
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    service
NameError: name 'service' is not defined
>>> service=(23,40,67)
>>> a
23
>>> type(a)
<class 'int'>
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=service*1.1
	else:
		result=service

>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    service_price()
  File "<pyshell#105>", line 5, in service_price
    result=service*1.1
TypeError: can't multiply sequence by non-int of type 'float'
>>> type(service)
<class 'tuple'>
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=service*1.1
	else:
		result=service

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:n
>>> 
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=service*1.1
	if valueAdded == 'n':
		result=service

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:n
>>> 
>>> result
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=service*int(1.1)
	else:
		result=service

		
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
>>> 
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
	   if service == 'a':
		result=23*1.1
	   if service == 'b':
		result=40*1.1
	   if service == 'c':
		result=67*1.1
	 if valueAdded == 'n':
	   if service == 'a':
		result=23
	   if service == 'b':
		result=40
	   if service =='c':
		result=67
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		if service == 'a':
			result=23*1.1
		if service == 'b':
			result=40*1.1
		if service == 'c':
			result=67*1.1
	if valueAdded == 'n':
		if service == 'a':
			result=23
		if service == 'b':
			result=40
		if service =='c':
			result=67

			
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=service*1.1
	if valueAdded == 'n':
		result=service
	print(round(result,1), '만 원입니다')

	
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    service_price()
  File "<pyshell#128>", line 5, in service_price
    result=service*1.1
TypeError: can't multiply sequence by non-int of type 'float'
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:n
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    service_price()
  File "<pyshell#128>", line 8, in service_price
    print(round(result,1), '만 원입니다')
TypeError: type str doesn't define __round__ method
>>> type(service)
<class 'tuple'>
>>> type(a)
<class 'int'>
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=service*2
	if valueAdded == 'n':
		result=service
	print(round(result,1), '만 원입니다')

>>> 
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    service_price()
  File "<pyshell#133>", line 8, in service_price
    print(round(result,1), '만 원입니다')
TypeError: type str doesn't define __round__ method
>>> type(result)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    type(result)
NameError: name 'result' is not defined
>>> def service_price():
	service=input('서비스 종류를 입력하세요, a/b/c:')
	valueAdded=input('부가세를 포함합니까? y/n:')
	if valueAdded == 'y':
		result=float(service*1.1)
	if valueAdded == 'n':
		result=float(service)
	print(round(result,1), '만 원입니다')

	
>>> service_price()
서비스 종류를 입력하세요, a/b/c:a
부가세를 포함합니까? y/n:y
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    service_price()
  File "<pyshell#138>", line 5, in service_price
    result=float(service*1.1)
TypeError: can't multiply sequence by non-int of type 'float'
>>> 