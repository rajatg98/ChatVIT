from code_timetable_data import *
import datetime
from nltk.chat.util import Chat, reflections


replacements = {
  'lol': 'laugh out loud',
  'y': 'why',
  'l8': 'late',
  'u': 'you',
  'r': 'are'
}

class Class:
  def __init__(self, coursecode,coursename,day):
    self.coursecode = coursecode
    self.coursename = coursename
    self.day = day


import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


ADict=dict()


Ans=[[["current","class"]],[["next","class"]],[["previous","class"]],[["left"]]]
Ans+=[   [["completed"]] , [["today","time","table"]],[["tomorrow","time","table"]],
         [["faculty"]],[["yesterday","time","table"]],[["mon","time","table"]],
         [["tue","time","table"]],[["wed","time","table"]],[["thu","time","table"]],
         [["fri","time","table"]],[["monday","time","table"]],[["tuesday","time","table"]],
         [["wednesday","time","table"]],[["thursday","time","table"]],[["friday","time","table"]]
        ]

for ii in range(len(Ans)):
    for jj in range(len(Ans[ii])):
        Ans[ii][jj]=tuple(sorted(Ans[ii][jj]))
        ADict[Ans[ii][jj]]=ii+1


StopWords=stopwords.words("english")
StopWords=set(StopWords)
Rr=["what","which","who","where","how","when"]
RR=["'s","'re","'ll"]
abbr={
        "nlp":"Natural Language Processing",
        "biodb":"Biological Database","bio":"Biological Database","biology":"Biological Database",
        "mmdd":"Molecular Modelling and Drug Design","drug":"Molecular Modelling and Drug Design",
        "ai":"Artificial Intelligence","artificial":"Artificial Intelligence",
        "cybersec":"Cyber Security","cyber":"Cyber Security",
        "tarp":"Technical Answers for Real World Problems (TARP)",
        "eco":"International Economics","economics":"International Economics","intl":"International Economics"
    }


for i in RR:
    StopWords.add(i)
for i in Rr:
    StopWords.remove(i)


HI=["hi","hello","there"]
HIa=["Hello Rajat!","How can I help you?","Hi!", "I am Candy, your assistant","Hi there!","Hello!","Namaste", "Wassup Rajat"]
HIac=-1

def Query1(query0):
    global HIac
    now = datetime.datetime.now()
    now=now+datetime.timedelta(minutes = 330)
    WeekDay=now.strftime("%a").upper()
    Hour=now.hour
    Minute=now.minute
    sentence=query0
    
    sentence=sentence.lower()
    words=word_tokenize(sentence)

    clean=[]

    for w in words:
        if w not in StopWords:
            clean.append(w)

    ans_string="Sorry! I didn't understand you!"
    clean=set(clean)

    for jjj in HI:
        if jjj in clean:
            HIac+=1
            return(HIa[HIac%len(HIa)])

    for x2 in ADict:
        if set(x2).issubset(clean):
            #print(x2)
            if set(x2)=={"faculty"}:
                ans_string=Query(8,0,0,query0)
                break
            else:
                ans_string=Query(ADict[x2],WeekDay,Hour,Minute)
                break

    return(ans_string)

