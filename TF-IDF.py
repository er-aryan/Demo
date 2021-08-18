import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = 'Sabudh is the foundation.'
documentB = 'It is located in Mohali.'

bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')

print(f"Bag of Words of A : {bagOfWordsA}")
print(f"Bag of Words of A : {bagOfWordsB}")
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
print()

numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

data = pd.DataFrame([numOfWordsA,numOfWordsB],index=["A","B"])
print(data)

# from nltk.corpus import stopwords
# stopwords.words('english')

def TF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = TF(numOfWordsA, bagOfWordsA)
tfB = TF(numOfWordsB, bagOfWordsB)
print()
print("TF values of A set :----\n")
print(tfA)
print()
print("TF values of B set :----\n")
print(tfB)

def IDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict
idfs = IDF([numOfWordsA,numOfWordsB])
print()
print("IDF values of sets are :----\n")
print(idfs)

def TFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

TFIDF_A = TFIDF(tfA, idfs)
TFIDF_B = TFIDF(tfB, idfs)
print()
print()
print("TF-IDF :---->\n")
TF_IDF = pd.DataFrame([TFIDF_A, TFIDF_B],index=["A","B"])
print(TF_IDF)

