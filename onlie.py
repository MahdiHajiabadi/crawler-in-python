import string
import urllib.request
import sys
address = input("Please enter an URL:   ")
a = urllib.request.urlopen(address)
x = a.read()
z = x.decode("utf-8")
for line in z.splitlines():
    STR = line
    STR = STR.replace(" ","")
    if STR.find('products-attribute-title')!= -1 or  STR.find('display: inline-block') != -1 or STR.find('products-attribute-value')!= -1:
        x1 = STR.find('">')
        x2 = STR.find('</')
        STR = STR[x1:x2]
        print(STR)
Link_Number=0
for line in z.splitlines():
    STR = line
    STR = STR.replace(" ","")
    if STR.find('div class')!= -1 or  STR.find('itemprop') != -1 or STR.find('description')!= -1 or STR.find('innerContent')!= -1:
        Link_Number+=1
        if (Link_Number == 1):
            print(STR)
            text = STR
address = 'http://www.mobile.ir/phones/comments-37874-samsung-galaxy-j2.aspx'
a = urllib.request.urlopen(address)
x = a.read()
z = x.decode("utf-8")
comments = open('C://Users//elnaz//Desktop//comments.txt','w')
Link_Number= 0
for line in z.splitlines():
    STR = line
    STR = STR.replace(" ","")
    if (STR.find('<br')!= -1):
        Link_Number+=1
        if (Link_Number>154):
           print(STR)
