#ftiagmeno se python 3.6.3
import random
for i in range(30):
    if i==0:
        a=[random.randint(-30,30)]
    else:
        a.append(random.randint(-30,30))
print(a)
count=0
for i in range(30):
    for j in range(30):
        if i!=j:
            x=(a[i]+a[j])*-1
            if x in a:
                h=a.index(x)
                print(a[i],a[j],a[h])
                count=count+1
if count==0:
    print("there isn't such numbers")

            

