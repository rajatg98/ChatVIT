
# Weekday abbreviations
WEEK=["MON","TUE","WED","THU","FRI","SAT","SUN"]
from dataload_init import *
import csv
import datetime
from collections import defaultdict as dd

abbr={
        "nlp":"Natural Language Processing",
        "biodb":"Biological Database","bio":"Biological Database","biology":"Biological Database",
        "mmdd":"Molecular Modelling and Drug Design","drug":"Molecular Modelling and Drug Design",
        "ai":"Artificial Intelligence","artificial":"Artificial Intelligence",
        "cybersec":"Cyber Security","cyber":"Cyber Security",
        "tarp":"Technical Answers for Real World Problems (TARP)",
        "eco":"International Economics","economics":"International Economics","intl":"International Economics"
    }


# next class for the day
def NextClass(W,H):
    for h in range(H+1,23):
        #print(h)
        p=CurClass(W,h,1)
        if p[1]==1:
            return(p[0])
    return("-1")


#current class
def CurClass(W,H,f=0):
    #D[1]=int(D[1])
    D=[W,H]
    if tuple(D) in RS:
        dslot=RS[tuple(D)]
        if dslot in RealTT:
            p=RealTT[dslot]
            return((p,1))
    if f==0:
        return((NextClass(W,H),0))
    else:
        return(("-1",0))


#previous class
def PreClass(W,H):
    for h in range(H-1,7,-1):
        #print(h)
        p=CurClass(W,h,1)
        if p[1]==1:
            return(p[0])
    return("-1")


#count of today's classes
def ClassCountToday(W,H):
    complete=0
    left=0
    for h in range(8,H):
        p=CurClass(W,h,1)
        if p[1]==1:
            complete+=1
    for h in range(H,21):
        p=CurClass(W,h,1)
        if p[1]==1:
            left+=1
    return([complete,left])


#today time table
def TodayTT(W):
    R=[]
    for h in range(8,21):
        p=CurClass(W,h,1)
        if p[1]==1:
            R.append((h,p[0]))
    return(R)


#time table
def weekTT(W):
    te = TodayTT(W)
    #print("    ",W)
    temp32="    %s\n"%W
    for x in te:
        p = MClass[x[1]]
        temp32+="          %d:00 - %d:50 : %s at %s\n"%(x[0],x[0],p.coursename,p.venue)
    temp32=temp32[:-1]
    return(temp32)


#query process
def Query(sel,WeekDay,Hour,Minute):

    temp32="---> > Error in Query < <---\n"
    if sel==1:
        #You don't have any current class\nBut your next class is %s
        te=CurClass(WeekDay,Hour)
        if te[1] ==0:
            if te[0]=="-1":
                temp32="You are done for today! No more Classes! Relax."
            else:
                p=MClass[te[0]]
                temp32="You don't have any current class\nBut your next class is %s- %s at %s"%(p.coursecode,p.coursename,p.venue)
        else:
            p=MClass[te[0]]
            temp32="Your current class is %s- %s at %s"%(p.coursecode,p.coursename,p.venue)
    
    elif sel==2:
        te=NextClass(WeekDay,Hour)
        if te=="-1":
            temp32="You have no next class! No more Classes! Relax."
        else:
            p=MClass[te]
            temp32="your next class is %s- %s at %s"%(p.coursecode,p.coursename,p.venue)

    elif sel==3:
        te=PreClass(WeekDay,Hour)
        if te=="-1":
            temp32="You had no previous class!"
        else:
            p=MClass[te]
            temp32="your previous class was %s- %s at %s"%(p.coursecode,p.coursename,p.venue)
    
    elif sel==4 or sel==5:
        te=ClassCountToday(WeekDay,Hour)
        temp32="Number of Completed Class : %d\n          Number of Upcoming Class : %d"%(te[0],te[1])
    
    elif sel==6:
        te = TodayTT(WeekDay)
        temp32="    %s\n"%WeekDay
        for x in te:
            p = MClass[x[1]]
            temp32+="          %d:00 - %d:50 : %s at %s\n"%(x[0],x[0],p.coursename,p.venue)
        temp32=temp32[:-1]
    
    elif sel==7:
        W=(WEEK)[(WEEK.index(WeekDay)+1)%7]
        te = TodayTT(W)
        temp32="    %s\n"%W
        for x in te:
            p = MClass[x[1]]
            temp32+="          %d:00 - %d:50 : %s at %s\n"%(x[0],x[0],p.coursename,p.venue)
        temp32=temp32[:-1]
    
    elif sel==9:
        W=(WEEK)[(WEEK.index(WeekDay)-1)%7]
        te = TodayTT(W)
        if W=="SUN" or W=="SAT":
            return("It was %s, So there were no classes!\n"%W)
        temp32="    %s\n"%W
        for x in te:
            p = MClass[x[1]]
            temp32+="          %d:00 - %d:50 : %s at %s\n"%(x[0],x[0],p.coursename,p.venue)
        temp32=temp32[:-1]
    
    elif sel==8:
        query=Minute.split(" ")
        query=[i.lower() for i in query]
        f="X"
        for s in query:
            if s in abbr:
                f=abbr[s]
                break
        if f=="X":
            return("No such course exists!")
        else:
            for cc in MClass:
                if cc.coursename == f:
                    return("The faculty for %s is %s"%(f,cc.facultyname))

    elif sel==10 or sel==15:
        return(weekTT("MON"))
    elif sel==11 or sel==16:
        return(weekTT("TUE"))
    elif sel==12 or sel==17:
        return(weekTT("WED"))
    elif sel==13 or sel==18:
        return(weekTT("THU"))
    elif sel==14 or sel==19:
        return(weekTT("FRI"))
    return(temp32)

print("Data Processing Completed. . .")



