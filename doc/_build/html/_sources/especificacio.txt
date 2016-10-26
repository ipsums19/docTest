Especificació
=============

.. toctree::
   :hidden:

   ex1

Donat un fitxer amb jocs de proves com :download:`ex1.txt`, si el
processem amb `doctest` obtindriem :download:`ex1-out.txt`, però el
resultat de processar-lo amb :py:mod:`doctestfdbk` hauria de ser el
del fitxer :download:`ex1.rst` que podem veure a :doc:`ex1` un cop
processat amb sphinx.

.. py:module:: doctestfdbk

El mòdul :py:mod:`doctestfdbk` definirà la funció següent:

.. py:function:: testfile(filename, module_relative=True, name=None, package=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, parser=DocTestParser(), encoding=None)

   Té els mateixos paràmetres i fa el mateix que
   :py:func:`doctest.testfile`. Només difereix en el format de la
   sortida.
