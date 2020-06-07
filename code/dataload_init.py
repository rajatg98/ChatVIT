import csv
import datetime
from collections import defaultdict as dd


class Class:
  def __init__(self, coursecode,coursename,slot,facultyname,venue):
    self.coursecode = coursecode
    self.coursename = coursename
    self.slot = slot
    self.venue = venue
    self.facultyname = facultyname



S=dict()
S["A1"]=[("MON",8),("WED",9) ]
S["B1"]=[("TUE",8),("THU",9) ]
S["C1"]=[("WED",8),("FRI",9) ]
S["D1"]=[("THU",8),("MON",10) ]
S["E1"]=[("FRI",8),("TUE",10) ]
S["F1"]=[("MON",9),("WED",10) ]
S["G1"]=[("TUE",9),("THU",10) ]

S["TA1"]=[("FRI",10)]
S["TB1"]=[("MON",11)]
S["TC1"]=[("TUE",11)]
S["TD1"]=[("FRI",12)]
S["TE1"]=[("THU",11)]
S["TF1"]=[("FRI",11)]
S["TG1"]=[("MON",12)]

S["TAA1"]=[("TUE",12)]
S["TCC1"]=[("THU",12)]


ss=list(S.keys())
for x in ss:
    y=x[:-1]+str(2)
    t=[]
    for f in S[x]:
        d=list(f)
        d[1]+=6
        d=tuple(d)
        t.append(d)
    S[y]=t
S["TD2"]=[("WED",17)]
S["TDD2"]=[("FRI",18)]

RS=dict()

for x in S:
    for y in S[x]:
        RS[y]=x

RealTT=dict()

MClass=[]
with open('timetable-copy.csv', 'r',encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[3][4]!='0' or row[3][6]!='0':
            continue
        Ctem=row[2]
        ccode=""
        i=0
        while(Ctem[i]!='-'):
            i+=1
        ccode=Ctem[:i].strip()

        j=len(Ctem)-1
        while(Ctem[j]!='-'):
            j-=1
        cname=Ctem[i+1:j].strip()

        cslot=row[7].split('+')
        cvenue=row[8]
        
        cffc=row[9].split('-')
        cfaculty=cffc[0].strip()
        
        p1=Class(ccode,cname,cslot,cfaculty,cvenue)
        idd=len(MClass)
        for i1 in cslot:
            RealTT[i1]=idd
        MClass.append(p1)

print("Data Loading Completed . . .")