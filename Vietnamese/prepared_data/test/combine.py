import codecs
with codecs.open('lhs.txt', 'r', encoding='utf-8') as lhs, codecs.open('rhs.txt', 'r', encoding='utf-8') as rhs, \
    codecs.open('test.txt', 'w') as ofile:
    lhsdata = []
    for line in lhs.readlines():
        lhsdata.append(line.strip())

    rhsdata = []
    for line in rhs.readlines():
        rhsdata.append(line.strip())

    for idx, ld in enumerate(lhsdata):
        ofile.write(ld + ' ' + rhsdata[idx] + '\n')
