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
           File "/usr/lib/python3.4/doctest.py", line 1324, in __run
             compileflags, 1), test.globs)
           File "<doctest ex1.txt[1]>", line 1, in <module>
             l[3]
         IndexError: list index out of range

   Seguiu l'enllaç IndexError_ per veure les possibles causes d'aquest
   error.

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
           File "/usr/lib/python3.4/doctest.py", line 1324, in __run
             compileflags, 1), test.globs)
           File "<doctest ex1.txt[3]>", line 1, in <module>
             a + b
         NameError: name 'a' is not defined

   Seguiu l'enllaç NameError_ per veure les possibles causes d'aquest
   error.

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
   
   El resultat obtingut no és el previst.

.. Enllaços als errors

.. _IndexError: http://gie.cs.upc.edu/fi/errors/errors.html#index-error
.. _NameError: http://gie.cs.upc.edu/fi/errors/errors.html#nameerror
