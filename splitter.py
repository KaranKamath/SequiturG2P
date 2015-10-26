import sys
import codecs
import random

fname = sys.argv[1]
trainProb = float(sys.argv[2])

print 'Train/Test: ', str(trainProb * 100), str((1-trainProb) * 100)

with codecs.open(fname, 'r', encoding='utf-8') as fr,\
    codecs.open('train.lex', 'w', encoding='utf-8') as ftr,\
    codecs.open('test.lex', 'w', encoding='utf-8') as ftst:

    for line in fr.readlines():
        if random.random() < trainProb:
            ftr.write(line)
        else:
            ftst.write(line)
   
