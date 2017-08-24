from os import listdir as ld
from functools import reduce

class File (object):

    def __init__(self, fileName=''):

        self.fileName = fileName
        self.data = ''
        self.words = []
        self.wordcnt = {}
        self.line = []

    def storeWords(self):

        fp = open(self.fileName, "r")
        self.data = fp.read().lower().replace('\n', ' ').replace('\r', '')
        self.words = self.data.split()
        fp.close()
        return self.words

    def getLine(self):

        return self.line

    def getFilename(self):

        return self.fileName

    def getWords(self):

        return  self.words

    def getData(self):

        return self.data

    def wordCount(self):

        r = ".,?!;:()=+-*/"
        s = ''
        for word1 in self.words:
            word = word1.strip(r)
            s = s+word
            if word not in self.wordcnt:
                self.wordcnt[word] = 0
            self.wordcnt[word] += 1
        self.line = s
        return self.wordcnt

def bagOfWords(file1, file2):

    file1.storeWords()
    file2.storeWords()
    words1 = file1.wordCount().keys()
    words2 = file2.wordCount().keys()
    wcnt1 = file1.wordCount()
    wcnt2 = file2.wordCount()
    dps = 0
    for word in words1:
        if word in words2:
            dps += wcnt1[str(word)] * wcnt2[str(word)]
    ss1 = 0
    for word in words1:
        ss1 += wcnt1[str(word)] * wcnt1[str(word)]

    ss2 = 0
    for word in words2:
        ss2 += wcnt2[str(word)] * wcnt2[str(word)]

    return dps*100/((ss1**0.5)*(ss2**0.5))

def stringMatching(file1, file2):

    file1.storeWords()
    file2.storeWords()
    file1.wordCount()
    file2.wordCount()
    string1 = file1.getData()
    string2 = file2.getData()
    maxsubstring = ''
    substring = string1[0]
    i = 0
    j = 0
    try:
        while True:
            if substring in string2:
                j += 1
                if len(substring) > len(maxsubstring):
                    maxsubstring = substring[:]
                substring = substring + string1[i + j]
            else:
                i += 1
                j = 0
                substring = string1[i]
    except:
        s = len(maxsubstring)
    l = len(string1)+len(string2)
    pd = (s*2/l)*100
    return pd

path = input().replace('\\', '/')
files = [p for p in ld(path) if p.endswith('.txt')]
print(' '*(len(max(files))+4),' ',end = '')
for i in range(len(files)):
    print('{:10}'.format(files[i]),'  ', end = '')
print('')
for i in range(len(files)):
    f1 = File(files[i])
    print(f1.getFilename(),'  ', end='')
    for j in range(len(files)):
        f2 = File(files[j])
        print('{:8.2f}'.format(bagOfWords(f1, f2)),'%','  ', end = '')
    print('')
print('--------------------------------')
print(' '*(len(max(files))+4),' ',end = '')
for i in range(len(files)):
    print('{:10}'.format(files[i]),'  ', end = '')
print('')
for i in range(len(files)):
    f1 = File(files[i])
    print(f1.getFilename(), ' ', end='')
    for j in range(len(files)):
        f2 = File(files[j])
        print('{:8.2f}'.format(stringMatching(f1, f2)),'%','  ', end = '')
    print('')