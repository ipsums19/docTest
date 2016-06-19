import doctest
from doctest import DocTestParser, DocTestRunner, Example
from myDocTestRunner import MyDocTestRunner

def testfile(filename, fileErrors):
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
    print(open(fileErrors,"r").read())

testfile("ex1.txt", "errors.txt")
