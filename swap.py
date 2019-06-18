Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them
enter the position 16 7 8 9
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 19, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 16, in main
    a,b=inputlist()
  File "/home/bmsce/pythprgms/swap.py", line 3, in inputlist
    pos1=int(input("enter the position 1"))
ValueError: invalid literal for int() with base 10: '6 7 8 9'
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them
enter the position 17 6 5 4
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 19, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 16, in main
    a,b,n=inputlist()
  File "/home/bmsce/pythprgms/swap.py", line 3, in inputlist
    pos1=int(input("enter the position 1"))
ValueError: invalid literal for int() with base 10: '7 6 5 4'
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them
enter the position 17 8 5 6
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 20, in <module>
    enter the numbers with space between them
  File "/home/bmsce/pythprgms/swap.py", line 17, in main
    ValueError: invalid literal for int() with base 10: '6 7 8 9'
  File "/home/bmsce/pythprgms/swap.py", line 3, in inputlist
    Type "help", "copyright", "credits" or "license()" for more information.
ValueError: invalid literal for int() with base 10: '7 8 5 6'
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them 5 6 78 9
enter the position 1 2
enter the position 2 3
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 20, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 18, in main
    c=swap(a,b)
TypeError: swap() missing 1 required positional argument: 'pos2'
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them99 7 5 3
enter the position 13
enter the position 2 2
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 20, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 19, in main
    d=ouput()
NameError: name 'ouput' is not defined
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them7 7 8 4 3
enter the position 1 2
enter the position 2 1
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 20, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 19, in main
    d=ouput(n)
NameError: name 'ouput' is not defined
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them
enter the position 15
enter the position 25
swapping impossible
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 27, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 24, in main
    a,b,n=inputlist()
TypeError: 'NoneType' object is not iterable
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them4 5 6 7
enter the position 13
enter the position 22
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 27, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 25, in main
    swap(n,a,b)
  File "/home/bmsce/pythprgms/swap.py", line 11, in swap
    n[pos1-1],n[pos2-1]=n[pos2-1],n(pos1-1)
TypeError: 'list' object is not callable
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them4 5 3 2
enter the position 12
enter the position 21
Traceback (most recent call last):
  File "/home/bmsce/pythprgms/swap.py", line 27, in <module>
    main()
  File "/home/bmsce/pythprgms/swap.py", line 26, in main
    ouput(n)
NameError: name 'ouput' is not defined
>>> 
=================== RESTART: /home/bmsce/pythprgms/swap.py ===================
enter the numbers with space between them4 5 3 2
enter the position 12
enter the position 21
['5', '4', '3', '2']
>>> 
