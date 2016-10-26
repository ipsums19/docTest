Implementació
=============

Idea General
------------
La idea era crear una nova funció testfile en la cual rebriem el fitxer.txt
que volem testejar, aquest fitxer el dividirem en 2 parts, la part del
doctest i la part dels strings. Anirem intercalan la sortida string, test. 

Primer Intent
-------------
Primer vam intentar pasar al runner els testos un per un, i que la funció
testfile sigues l'encarragat de printar per ordre els strings i els test.
Llavors el problema que teniem es que tots els exemples s'havien d'executar
en un mateix doctest, com s'argumenta en la pàgina de python_, ja que han de
mantenir el mateix namespace.

.. _python: https://docs.python.org/3/library/doctest.html#doctest-objects 

Segona Implementació
--------------------
El segon intent va ser que la nostra clase myDocTestRunner imprimis ell 
directament ja la sortida intercalada amb string, test. Per aixó abans 
d'executar el nostre runner el que fem es asignar-li un nou atribut 
strings el cual fara la funció de cua. Així el runner abans de imprimir
cada test el primer que farà és imprimir el primer string de la llista
i eliminar-lo.


Class myDocTestRunner
---------------------
.. autoclass:: doctestfdbk.MyDocTestRunner
    :members:

Funció testfile2
----------------
.. autofunction:: doctestfdbk.testfile
    
