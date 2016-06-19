import doctest
import traceback
import re

def ident(lines, amount, ch=' '):
    padding = amount * ch
    return padding + ('\n' + padding).join(lines.split('\n'))

def getExampleString(example):
        if example.want == "":
            return ">>> " + example.source
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
    def report_start(self, out, test, example):
        pass

    def report_success(self, out, test, example, got):
        out(self.strings.pop(0) + getExampleString(example))

    def report_failure(self, out, test, example, got):
        out(self.strings.pop(0) + getExampleString(example) + getErrorString(example.source) + getFailureString(example.want, got) )

    def report_unexpected_exception(self, out, test, example, exc_info):
        out(self.strings.pop(0) + getExampleString(example) + getErrorString(example.source) +
                ident("\nException raised:", 5) + "\n" + ident(traceback.format_exc(exc_info),9) +
                "\n" + ident("Seguiu l'enllac " + getError(exc_info) + " per veure les possibles causes\n",3))
