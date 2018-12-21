# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
hh=int(sys.stdin.readline())
mm=int(sys.stdin.readline())
msg=""
hour={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'one'}
ex={10:'ten',11:'eleven',12:'twelve',13:'thirteen',18:'eighteen',20:'twenty'}
minutes=mm
def zerofunc(hh):
    return str(hour[hh])+" o' clock"

def prefunc(hh,mm):
    if mm==15:
        return "quarter past "+hour[hh]
    if mm==1:
        return "one minute past "+hour[hh]
    if ex.has_key(mm):
        return ex[mm]+" minutes past "+hour[hh]
    if mm>1 and mm<9:
        return hour[mm]+" minutes past "+hour[hh]
    if mm>13 and mm<20:
        return hour[mm%10]+"teen minutes past "+hour[hh]    
    if mm>20 and mm<30:
        return "twenty "+hour[mm%20]+" minutes past "+hour[hh]
    pass

def postfunc(hh,mm):
    if mm==45:
        return "quarter to "+hour[hh+1]
    if mm==59:
        return "one minute to "+hour[hh+1]
    minutes=60-mm
    if ex.has_key(minutes):
        return ex[minutes]+" minutes to "+hour[hh+1]
    if minutes>1 and minutes<9:
        return hour[minutes]+" minutes to "+hour[hh+1]
    if minutes>13 and minutes<20:
        return hour[minutes%10]+"teen minutes to "+hour[hh+1]    
    if minutes>20 and minutes<30:
        return "twenty "+hour[minutes%20]+" minutes to "+hour[hh+1]
    
    pass
def onfunc(hh):
    return "half past "+hour[hh]
if mm==0:
    msg=zerofunc(hh)
    pass
if mm==30:
    msg=onfunc(hh)
    pass
if mm>30:
    msg=postfunc(hh,mm)
    pass
if mm<30 and mm!=0:
    msg=prefunc(hh,mm)
    pass
print msg


