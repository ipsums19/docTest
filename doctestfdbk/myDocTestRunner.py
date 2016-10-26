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
import traceback
import re

def ident(lines, amount, ch=' '):
    padding = amount * ch
    return padding + ('\n' + padding).join(lines.split('\n'))

def getExampleString(example):
        if example.want == "":
            return ">>> " + example.source[:-1]
        else :
            return ">>> " + example.source + example.want[:-1]

def getErrorString(source):
    return "\n\n.. error::\n\n" + ident("::",3) + "\n\n" + ident("Failed example:", 5) + "\n" + ident(source[:-1],9)

def getFailureString(want, got):
    return "\n" + ident("Expected:", 5) + "\n" + ident(want[:-1],9) + "\n" + ident("Got:", 5) + "\n" + ident(got,9)

def getError(exc_info):
    s = re.search('([A-Z])\w*', str(exc_info[0]))
    return s.group(0) + "_"

class MyDocTestRunner(doctest.DocTestRunner):
    """La nostre classe MyDocTestRunner heretada de la classe DocTestRunner del modul doctest
    simplement fa una variacio en el output de la classe. On la sortida sera sempre primer
    un string, el cual sera introduit per la funcio testfile, i despres l'execucio de un test"""

    def report_start(self, out, test, example):
        pass

    def report_success(self, out, test, example, got):
        """Funcio que executa la classe DocTestRunner en cas que el example sigui realitzat correctament,
        modificant el parametre out per tal que la sortida sigui la esperada.

        :param out: el output de la funcio
        :param test: el test que conte l'example
        :param example: es el example que es procesat
        :param got: el resultat obtingut """
        out(self.strings.pop(0) + ident(getExampleString(example), example.indent) + "\n")

    def report_failure(self, out, test, example, got):
        """Funcio que executa la classe DocTestRunner en cas que el example sigui realitzat correctament
        pero la sortida no sigui la esperada. Modifica el parametre out per tal que la sortida sigui la esperada.

        :param out: el output de la funcio
        :param test: el test que conte l'example
        :param example: es el example que es procesat
        :param got: el resultat obtingut"""
        out(self.strings.pop(0) + ident(getExampleString(example) + getErrorString(example.source) +
            getFailureString(example.want, got), example.indent) + "\n" )

    def report_unexpected_exception(self, out, test, example, exc_info):
        """Funcio que executa la classe DocTestRunner en cas que el example no s'executi correctamet.
        Modifica el parametre out per tal que la sortida sigui la esperada.

        :param out: el output de la funcio
        :param test: el test que conte l'example
        :param example: es el example que es procesat
        :param got: el resultat obtingut"""
        out(self.strings.pop(0) + ident(getExampleString(example) + getErrorString(example.source) +
                ident("\nException raised:", 5) + "\n" + ident("".join(traceback.format_exception(*exc_info)),9) +
                "\n" + ident("Seguiu l'enllac " + getError(exc_info) + " per veure les possibles causes\n",3),example.indent) + "\n")
