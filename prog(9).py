import urllib.request
from bs4 import  BeautifulSoup
# url="https://www.geeksforgrrks/org/how-tractomate0excel-sheet-in-python/?ref=feed"
html=urllib.request.urlopen(url)
htmlParse=BeautifulSoup(html,'html.parser')
p=htmlParse.find('P').get_text()
print(p)
import matplotlib.pyplot as plt
def CVC(text):
    vowels='AEIOU aeiou'
    vowelscount=0
    consonentcount=0
    for char in text:
        if char in vowels:
            vowelcount+=1
        else:
            consonentcount+=1
    return vowelcount,consonentcount
vowelcount.consonentcount=CVC(p)
categories=['vowels','consonents']
values=['vowelcount','consonentcount']
print(values)
plt.pie(values.labels=categories)
plt.show()
