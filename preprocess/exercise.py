#-*- encoding:UTF-8 -*-
import nltk
from nltk.corpus import PlaintextCorpusReader

corpus_root='C:/workspace/python/project/autodialog/db'
wordlists=PlaintextCorpusReader(corpus_root,'.*')
text=wordlists.words('post.txt')
bigrams=nltk.bigrams(text)
cfd=nltk.ConditionalFreqDist(bigrams)
# cfd.plot()
record=[]
for word in cfd:
    print(word.encode('gbk','ignore').decode('gbk'),' ',cfd[word].max().encode('gbk','ignore').decode('gbk'))