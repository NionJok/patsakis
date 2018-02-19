import random

timh = input("Δώσε το όνομα του αρχείου που έχει το κείμενο και μαζί με το type που είναι π.χ.: ασκηση10.txt(το κειμενο να είναι στο ίδιο φάκελο με την άσκηση)")
#apo8ikeyei se mia metavlhth to arxeio poy dinei o xrhsths
timh = timh.rstrip()
text_file = open(timh,"r")
#apo8ikeyei se enan pinaka tis le3is
lines = text_file.read().split(" ")
#metritis twn pezwn le3ewn
lower_number = 0
#pinakas gia tis pezes le3is
lower_case= []
#vriskei tis pezes le3eis kai tis apo8ikeyei se enan pinaka
for i in range (0, len(lines)):
    if lines[i]==lines[i].lower():
        lower_number = lower_number + 1
for i in range (0, lower_number):
    if lines[i]==lines[i].lower():
        lower_case.append(lines[i])
#pinakas gia tis triades poy 8a ftiaxtoyn mesa apo aytes tis le3is 
triades=[]
#poses triades epitrepete na ftiaxtoyn vasi twn pezwn poy vrikame
numbers_triades= len(lower_case)- 3
#ftiaxnei tis triades aytes
for i in range (0 ,numbers_triades):
    triades.append('')
    if i==0:
        for j in range (0,3):
            if j!=0:
                triades[i]=(triades[i]+" "+lower_case[j].replace('.', ' '))
            else:
                triades[i]=(triades[i]+lower_case[j].replace('.', ' '))
    else:
        
        for j in range (i,i+3):
            if j!=i:
                triades[i]=(triades[i]+" "+lower_case[j].replace('.', ' '))
            else:
                triades[i]=(triades[i] + lower_case[j].replace('.', ' '))
#metritis twn le3ewn 
words=3
#3ekinaei to kimeno apo mia random triada
keimeno=random.choice(triades)
#metritis wste na doyme ama 3ekinaei mia le3i apo tis dio teleytaies le3is tis proigoymenis le3is
metrhths=0

for i in range (0,numbers_triades):
    if keimeno==triades[i]:
        j=i
    
while words<=200:
    #pinakas gia tis 2 le3is poy arxizoyn me tis dio proigoymenes le3is
    same=[]
    spasmeno=triades[j].split(" ")
    for i in range(0, numbers_triades):
        spasmeno_test=triades[i].split(" ")
        if spasmeno[1]== spasmeno_test[0] and spasmeno[2]==spasmeno_test[1]:
            find=triades[i]
            same.append(find)
            metrhths=metrhths+1
            
    if metrhths>0:
        rand=random.choice(same)
        keimeno=keimeno+" "+rand
        metrhths=0
        
    else:
        rand=random.choice(triades)
        keimeno=keimeno+"."+rand
        for k in range (0,numbers_triades):
            if rand==triades[k]:
                j=k
    for z in range (0,numbers_triades):
        if triades[z]==rand:
            j=z
    words= words+3

print (keimeno)
    
        
    
    
    
    
    
    
        

