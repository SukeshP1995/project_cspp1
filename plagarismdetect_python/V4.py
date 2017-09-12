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
        self.data = fp.read().lower()
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
        print(self.wordcnt)
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

    return str(dps*100/((ss1**0.5)*(ss2**0.5)))+'%'

def stringMatching(file1, file2):
    file1.storeWords()
    file2.storeWords()
    file1.wordCount()
    file2.wordCount()
    line1 = file1.getLine()+' '
    line2 = file2.getLine()+' '
    data1 = file1.getData()
    data2 = file2.getData()
    i = 0
    counts = []
    count = 0
    while i <len(line1):

        j = 0
        while j < len(line2) and i <len(line1):
            if line1[i] == line2[j]:
                count += 1
                i += 1

            else:
                if count>0:
                    counts.append(count)
                count = 0
            j += 1
        i += 1

    s = reduce(lambda x, y: x*y, counts)
    l = len(data1)+len(data2)
    pd = (s/l)*100
    return str(pd)+'%'

path = 'F:/CSPP1/project/project_cspp1'
files = [p for p in ld(path) if p.endswith('.txt')]

for i in range(len(files)):
    f1 = File(files[i])
    for j in range(i+1,len(files)):
        f2 = File(files[j])
        print(f1.getFilename(),f2.getFilename())
        print('bag of words:',bagOfWords(f1, f2))
        print('string matching:',stringMatching(f1, f2))