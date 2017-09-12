from os import listdir as ld


class File (object):
    """
    class for file handling
    """

    def __init__(self, fileName=''):
        """
        Intialisation
        :param fileName: 'str'
            Receives a file name
        """
        self.fileName = fileName
        self.data = ''
        self.words = []
        self.wordcnt = {}
        self.line = []

    def storeWords(self):
        """
        Store words into a list
        :return: 'list' of 'str'
            data converted into words
        """

        fp = open(self.fileName, "r")
        self.data = fp.read().lower().replace('\n', ' ').replace('\r', '')
        self.words = self.data.split()
        fp.close()
        return self.words

    def getFilename(self):
        """
        Method to get the file name
        :return: 'str'
            name of the file
        """
        return self.fileName

    def getWords(self):
        """
        Method to get words inside the file
        :return: 'list' of 'str'
            list of words
        """
        return  self.words

    def getData(self):
        """
        Method to get data inside the file
        :return: 'str'
            data inside the file
        """
        return self.data

    def wordCount(self):
        """
        Method to count the number of individual words and store them into a dictionary
        :return: 'dict' of 'keys' in 'str' and 'values' in 'int'
        """
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
    """
    :param file1: 'str'
    :param file2: 'str'
        file names
    :return: 'float'
        plagiarism percentage between two files through Bag of words method
    """
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

    try:
        return dps*100/((ss1**0.5)*(ss2**0.5))
    except Exception as e:
        return 0
    

def stringMatching(file1, file2):
    """
    :param file1: 'str'
    :param file2: 'str
        file names
    :return: 'float'
        Plagiarism percentage between two files through String matching technique
    """

    file1.storeWords()
    file2.storeWords()
    file1.wordCount()
    file2.wordCount()
    string1 = file1.getData()
    string2 = file2.getData()
    maxSubString = ''
    if string1 == string2:
        return 100.0
    
    i = 0
    j = 0
    try:
        subString = string1[0]
        while True:
            if subString in string2:
                j += 1
                if len(subString) > len(maxSubString):
                    maxSubString = subString[:]
                subString = subString + string1[i+j]
            else:
                i += 1
                j = 0
                subString = string1[i]
    except:
        s = len(maxSubString)
        l = len(string1)+len(string2)
    try:
        pd = (s*2/l)*100
        return pd
    except:
        return 0.0

def method1() :
    '''
    function for Bag of words
    '''
    path = input('enter path of the file: ').replace('\\', '/')
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
            print('{:10.2f}'.format(bagOfWords(f1, f2)),'  ', end = '')
        print('')

def method2() :
    '''
    function for Sting matching
    '''
    path = input('enter path of the file: ').replace('\\', '/')
    files = [p for p in ld(path) if p.endswith('.txt')]
    print(' '*(len(max(files))+4),' ',end = '')
    for i in range(len(files)):
        print('{:10}'.format(files[i]),'  ', end = '')
    print('')
    for i in range(len(files)):
        f1 = File(files[i])
        print(f1.getFilename(), ' ', end='')
        for j in range(len(files)):
            f2 = File(files[j])
            print('{:10.2f}'.format(stringMatching(f1, f2)),'  ', end = '')
        print('')

def choice() :
    inp = int(input('enter 1 for bag of words \n     2 for string matching:  '))
    if inp == 1:
        method1()
    if inp == 2:
        method2()
choice()