class File (object):

    def __init__(self, fileName=''):

        self.fileName = fileName
        self.data = ''
        self.words = []
        self.wordcnt = {}

    def storeWords(self):

        fp = open(self.fileName, "r")
        self.data = fp.read().lower()
        self.words = self.data.split()
        fp.close()
        return self.words

    def getFilename(self):

        return self.fileName

    def getWords(self):

        return  self.words

    def getData(self):

        return self.data


    def wordCount(self):

        r = ".,?!;:()_=+-*/"
        for word1 in self.words:
            word = word1.strip(r)
            if word not in self.wordcnt:
                self.wordcnt[word] = 0
            self.wordcnt[word] += 1
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

    return str(dps*100/(ss1**0.5*ss2**0.5))+'%'




file1 = File("file1.txt")
file2 = File("file2.txt")

print(bagOfWords(file1, file2))
