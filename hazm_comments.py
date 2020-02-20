# coding=utf-8
from __future__ import unicode_literals
import codecs
from hazm import *
print("HIIII")
def hazmOnComment(filename):
    file = codecs.open(filename ,'r', encoding='utf-8')
    file_hazm = codecs.open('file_hazm.txt','w', encoding='utf-8')
    file_normalize_result = codecs.open('normalize','w', encoding='utf-8')
    file_stemmer_result = codecs.open('stemmer','w' ,encoding='utf-8')
    file_lemmatize_result = codecs.open('lemmatize' ,'w', encoding='utf-8')
    normalizer = Normalizer()
    stemmer = Stemmer()
    lemmatizer = Lemmatizer()
    for line in file:
        # normaaaliiizzzzzzz
        line = normalizer.normalize(line)
        file_normalize_result.write(line + "\n")
        line = line.split()
        for word in line:
            word = stemmer.stem(word)
            # steeemmmmmmmmmmmm
            file_stemmer_result.write(word )
            # lemetiiiiizzzzzzzz
            word = lemmatizer.lemmatize(word)
            file_lemmatize_result.write(word)
            file_hazm.write(word)
    file_hazm.close()
    file.close()
    file_normalize_result.close()
    file_stemmer_result.close()
    file_lemmatize_result.close()

if __name__ == "__main__":
    filename = "/home/khsh/Desktop/comments.txt"
    hazmOnComment(filename)