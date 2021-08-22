import time

def isOver(var, lim):
    if var>lim:
        riport=1
        var-=lim
    else:
        riport=0
    return var, riport


def es():
    try:
        
        now=time.strftime("%d/%m/%Y/%H:%M:%S")
        
        lstnow=now.split("/")
        daysTime=lstnow[3].split(":")
        #sec
        riport=0
        secTimeAft=(int(daysTime[2])+30)
        secTimeAft, riport= isOver(secTimeAft+riport, 60)
        #min
        
        minTimeAft, riport= isOver(int(daysTime[1])+50+riport, 60)

        #hour

        hourTimeAft, riport=isOver(int(daysTime[0])+17+riport, 24)

        #day

        dayTimeAft, riport=isOver(int(lstnow[0])+15+riport, 31)

        #m

        mTimeAft, riport=isOver(int(lstnow[1])+8+riport, 12)

        #year

        yearTimeAfter=int(lstnow[2])+31+riport

        lstafter=[str(dayTimeAft), str(mTimeAft),str(yearTimeAfter), str(hourTimeAft), str(minTimeAft), str(secTimeAft)]
        
        after=lstafter[0]+"/"+lstafter[1]+"/"+lstafter[2]+"/"+lstafter[3]+":"+lstafter[4]+":"+lstafter[5]
        return after
    except ValueError:
        raise Exception("something goes wrong")