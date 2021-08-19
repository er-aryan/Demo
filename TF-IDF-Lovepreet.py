import pandas as pd
import math


documentA = 'I have been working on some projects'
documentB = 'There are many projects to work on'
documentC = 'for working professionals vaccations are like a dream'

bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')
bagOfWordsC = documentC.split(' ')

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB)).union(set(bagOfWordsC))

num_of_words_A = dict(zip(uniqueWords, [0]*len(uniqueWords)))

for word in bagOfWordsA:
    num_of_words_A[word]+=1

num_of_words_B = dict(zip(uniqueWords, [0]*len(uniqueWords)))

for word in bagOfWordsB:
    num_of_words_B[word]+=1

num_of_words_C = dict(zip(uniqueWords, [0]*len(uniqueWords)))

for word in bagOfWordsC:
    num_of_words_C[word]+=1

print("------------------------------------------------------------------------------------")
print(num_of_words_A)
print("------------------------------------------------------------------------------------")
print(num_of_words_B)
print("------------------------------------------------------------------------------------")
print(num_of_words_C)
print("------------------------------------------------------------------------------------")

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = computeTF(num_of_words_A, bagOfWordsA)
tfB = computeTF(num_of_words_B, bagOfWordsB)
tfC = computeTF(num_of_words_C, bagOfWordsC)

print(tfA)
print("------------------------------------------------------------------------------------")
print(tfB)
print("------------------------------------------------------------------------------------")
print(tfC)
# print("---------------------->>>>>>>>>>>>>", tfC['professionals'])
print("------------------------------------------------------------------------------------")

def computeIDF(documents):
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

idfs = computeIDF([num_of_words_A, num_of_words_B, num_of_words_C])
print(idfs)
print("------------------------------------------------------------------------------------")

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        # if(word == 'professionals'):
        #     print("\n\n\n\n\n\n")
        #     print(val , idfs[word])
        tfidf[word] = val * idfs[word]
    return tfidf
# print(idfs['professionals'])
tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
tfidfC = computeTFIDF(tfC, idfs)

df = pd.DataFrame([tfidfA, tfidfB, tfidfC])
df.to_csv("./data.csv")
print(df)