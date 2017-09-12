from os import listdir as ld
class File (object):

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

def hash_values(s):
    """
    function to find hash values
    :param s: 'list' of 'str'
        list containing all the words in the file
    :return: 'list' of 'int'
        list containing all the hash values
    """
    l=[]
    for i in range(len(s)-5):
        a=0
        summ=0
        for j in range(i,i+5):
            summ=summ+ord(s[j])*(5**a)
            a+=1
        summ=summ%10007
        l.append(summ)
    return l


def finger(file1, file2):
    """
    fingerprinting process to find plagiarism percentage
    :param file1: 'str'
    :param file2: 'str'
        file names
    :return: 'int'
        plagiarism percentage through fingerprinting
    """

    file1.storeWords()
    file2.storeWords()
    file1.wordCount()
    file2.wordCount()
    l1 = file1.getData()
    l2 = file2.getData()

    l1=hash_values(l1)

    l2=hash_values(l2)

    l3=list(set(l1))

    c=0
    for char in l3:
        l=[i for i,x in enumerate(l2) if x==char]
        c=c+len(l)
    p=(c*2)/(len(l1)+len(l2))
    return (p*100)

def method1() :
    '''
    function for calling fingerprinting
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
            print('{:10.2f}'.format(finger(f1, f2)),'%','  ', end = '')
        print('')
method1()