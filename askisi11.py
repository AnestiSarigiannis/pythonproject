#ftiagmeno se python 3.6.3
import random
lex=[]
        
for i in range(100):
    lex.append([])
    for j in range(100):
        x=random.randint(1,26)
        if j==0:
            if x==1:
                a = ["A"]
            elif x==2:
                a = ["B"]
            elif x==3:
                a = ["C"]
            elif x==4:
                a = ["D"]
            elif x==5:
                a = ["E"]
            elif x==6:
                a = ["F"]
            elif x==7:
                a = ["G"]
            elif x==8:
                a = ["H"]
            elif x==9:
                a = ["I"]
            elif x==10:
                a = ["J"]
            elif x==11:
                a = ["K"]
            elif x==12:
                a = ["L"]
            elif x==13:
                a = ["M"]
            elif x==14:
                a = ["N"]
            elif x==15:
                a = ["O"]
            elif x==16:
                a = ["P"]
            elif x==17:
                a = ["Q"]
            elif x==18:
                a = ["R"]
            elif x==19:
                a = ["S"]
            elif x==20:
                a = ["T"]
            elif x==21:
                a = ["U"]
            elif x==22:
                a = ["V"]
            elif x==23:
                a = ["W"]
            elif x==24:
                a = ["X"]
            elif x==25:
                a = ["Y"]
            else:
                a = ["Z"]
        else:
            if x==1:
                a.append("A")
            elif x==2:
                a.append("B")
            elif x==3:
                a.append("C")
            elif x==4:
                a.append("D")
            elif x==5:
                a.append("E")
            elif x==6:
                a.append("F")
            elif x==7:
                a.append("G")
            elif x==8:
                a.append("H")
            elif x==9:
                a.append("I")
            elif x==10:
                a.append("J")
            elif x==11:
                a.append("K")
            elif x==12:
                a.append("L")
            elif x==13:
                a.append("M")
            elif x==14:
                a.append("N")
            elif x==15:
                a.append("O")
            elif x==16:
                a.append("P")
            elif x==17:
                a.append("Q")
            elif x==18:
                a.append("R")
            elif x==19:
                a.append("S")
            elif x==20:
                a.append("T")
            elif x==21:
                a.append("U")
            elif x==22:
                a.append("V")
            elif x==23:
                a.append("W")
            elif x==24:
                a.append("X")
            elif x==25:
                a.append("Y")
            else:
                a.append("Z")
    lex[i]=a
print(lex)
row=[[row[i] for row in lex] for i in range(100)]#kanw tis grammes stiles gia na elenxw an oi lexeis tou keimenou uparxoun katheta ston pinaka
print(row)
words=0
with open("userfile.txt", mode="r",encoding="utf-8") as my_file:
    for line in my_file:
        x=len(line)
        for i in range(100):
            y=0
            r=0
            for j in range(100):
                if line[y]==lex[i][j]:
                    y+=1
                    if y==x:
                        print(line)
                        y=0
                        words+=1
                        continue
                else:
                    y=0
        for i in range(100):
            for j in range(100):
                if line[r]==row[i][j]:
                    r+=1
                    if r==x:
                        print(line)
                        r=0
                        words+=1
                        continue
                else:
                    r=0
if words==0:
    print("there is not any common words in the file and the list")
                
                
                
