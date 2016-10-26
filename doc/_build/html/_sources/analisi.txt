Anàlisi
=======

:py:mod:`doctest`
-----------------

- La classe :py:class:`~doctest.DocTestParser` proporciona el mètode
  :py:meth:`~doctest.DocTestParser.parse` que obté una llista on
  s'intercalen *strings* amb exemples (:py:class:`~doctest.Example`).

- La classe :py:class:`~doctest.DocTestRunner` proporciona els mètodes
  :py:meth:`~doctest.DocTestRunner.report_start`,
  :py:meth:`~doctest.DocTestRunner.report_success`,
  :py:meth:`~doctest.DocTestRunner.report_unexpected_exception` i
  :py:meth:`~doctest.DocTestRunner.report_failure` per personalitzar la
  sortida.

- Probablement n'hi hauria prou amb una nova implementació de la
  funció :py:func:`~doctest.testfile` i amb una classe derivada de
  :py:class:`~doctest.DocTestRunner` que redefineixi el mètodes
  anteriors.

