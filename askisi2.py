#ftiagmeno se python 2.7.14
import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
for i in range(10):
    while True:
        num=input("please type a number between 1-80: ")
        if num>0:
            if num<81:
                break
    if i==0:
        pin=[num]
    else:
        pin.append(num)
print(pin)
success=[]
max=-1
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(pin,tmp))
    sum=0
    for j in range(180):
        if r[j]>3:
            sum+=1
    success.append(sum)
    if sum>max:
        max=sum
        maxday=cur_date
print success
print "the user had the most successful guesses at",maxday,"with",max,"right guesses"

        
    

