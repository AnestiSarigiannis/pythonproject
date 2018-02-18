#ftiagmeno se python 3.6.3
import random
sum=0
for i in range(1000):
    for j in range(500):
        if j==0:
            a=[random.randint(1,80)]
        else:
            a.append(random.randint(1,80))
    print(a)
    for h in range(100):
        if h==0:
            bingo=[0]#o pinakas autos deixnei posoi arithmoi exoun sbistei se kathe paikti wste na stamataw sto 5
        else:
            bingo.append(0)
    stop=0
    controlx=[]
    while stop==0:
        x=random.randint(1,80)
        print(x)
        if x in controlx:#elegxos gia tin apofigh klirwshs idiou arithmou
            continue
        else:
            controlx.append(x)
            if x in a:
                count=a.count(x)# to count einai poses fores iparxei ston pinaka h metabliti x wste na xerw poses epanalipseis na kanw
                flag=0
                while flag<count:
                    for pointer in range(500):
                        if x==a[pointer]:
                            bingo[pointer//5]=bingo[pointer//5]+1
                            flag=flag+1
                    print(bingo)
                sum+=1
        if max(bingo)>4:
            stop=1
average=sum/1000
print(average)
                
        
    
