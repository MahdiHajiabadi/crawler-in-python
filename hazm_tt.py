from __future__  import unicode_literals
import codecs
from hazm import *
from hazm import Lemmatizer,Stemmer,Normalizer
normalizer = Normalizer()
file = codecs.open('/home/khsh/Desktop/comments.txt' ,'r', encoding='utf-8')
normalizer = Normalizer()
stemmer = Stemmer()
l = Lemmatizer()
file_normalize = open('/home/khsh/Desktop/Normalize.txt' , 'w')
file_stemmer = open('/home/khsh/Desktop/Stemmer.txt' , 'w')
file_lemmatizer = open('/home/khsh/Desktop/Lemmatizer.txt' , 'w')
for line in file:
        # normaaaliiizzzzzz
        line = normalizer.normalize(line)
        file_normalize.write(line.encode('utf-8'))
        file_normalize.write("\n")
        line = line.split()
        for word in line:
            word1 = stemmer.stem(word)
            # steeemmmmmmmmmmmm
            file_stemmer.write(word1.encode('utf-8'))
            file_stemmer.write(" ")
            word2 = l.lemmatize(word)
            file_lemmatizer.write(word2.encode('utf-8'))
            file_lemmatizer.write(" ")


            # lemetiiiiizzzzzzzz
file_normalize.close()
file_lemmatizer.close()
file_stemmer.close()
