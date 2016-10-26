# Copyright 2016
# Author Joan Barba
# This file is part of doctestfdbk.

# doctestfdbk is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# doctestfdbk is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with doctestfdbk.  If not, see <http://www.gnu.org/licenses/>.
import doctest
from doctest import DocTestParser, DocTestRunner, Example
from .myDocTestRunner import MyDocTestRunner

def testfile(filename, fileErrors):
    """Funció testfile() que rep per paràmetres el filename que seria el fitxer
    doctest que volem mostrar per pantalla, i el fitxer fileErrors que serà
    els links dels errors que volem mostrar. La funció crearà una instància
    de myDocTestRunner, i instanciarà un paràmetre strings que serà una llista
    d'strings els cuals l[n] i l[n+1] seran els strings en el cual el n text estarà
    entremig"""
    fitxer = open(filename,"r").read()
    l = DocTestParser().parse(fitxer)

    l1 = []
    for i in l:
        if isinstance(i,str):
            l1.append(i)
    l2 = DocTestParser().get_examples(fitxer)

    mapp = dict()
    doc = doctest.DocTest(l2, mapp, "", None, None, None)

    runner = MyDocTestRunner()
    runner.strings = l1
    runner.run(doc)

    print("\n.. Enllacos als errors")
    with open(fileErrors,"r") as f:
        print(f.read())
