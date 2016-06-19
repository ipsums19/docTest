Exemple 1
=========


Indexar fora del límits
-----------------------

Aquest exemple ha de produir l'exepció d'accés fora dels límits.

>>> l = [0, 1, 2]
>>> l[3]
3

.. error::

   ::

     Failed example:
         l[3]     
     Exception raised:
         Traceback (most recent call last):
           File "/usr/lib/python2.7/doctest.py", line 1315, in __run
             compileflags, 1) in test.globs
           File "<doctest [1]>", line 1, in <module>
         IndexError: list index out of range
         
   Seguiu l'enllac IndexError_ per veure les possibles causes
   
Si accedim dins dels límits, tot va bé.

>>> l[2]
2

Variable no inicialitzada
-------------------------

Ús d'una variable abans d'inicialitzar-la.

>>> b = 3
>>> a + b
3

.. error::

   ::

     Failed example:
         a + b     
     Exception raised:
         Traceback (most recent call last):
           File "/usr/lib/python2.7/doctest.py", line 1315, in __run
             compileflags, 1) in test.globs
           File "<doctest [4]>", line 1, in <module>
         NameError: name 'a' is not defined
         
   Seguiu l'enllac NameError_ per veure les possibles causes
   
Si inicialitzem `a` el resultat és el previst.

>>> a = 0
>>> a + b
3

El resultat difereix
--------------------

El resultat obtingut no és el previst.

>>> 2 + 2
5

.. error::

   ::

     Failed example:
         2 + 2
     Expected:
         5
     Got:
         4
         
.. Enllacos als errors

.. _IndexError: http://gie.cs.upc.edu/fi/errors/errors.html#index-error
.. _NameError: http://gie.cs.upc.edu/fi/errors/errors.html#nameerror

